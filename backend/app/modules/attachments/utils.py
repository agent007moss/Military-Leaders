# app/modules/attachments/utils.py

from __future__ import annotations

import os
from pathlib import Path
from typing import Tuple
from uuid import uuid4


# ----------------------------------------------------------------------
# Resolve project root safely (3 parents up from this file):
#   attachments/utils.py
#   attachments/
#   modules/
#   app/
#   backend root is **parents[3]**
# ----------------------------------------------------------------------
try:
    _PROJECT_ROOT = Path(__file__).resolve().parents[3]
except Exception:
    # Extremely defensive fallback (should never happen)
    _PROJECT_ROOT = Path.cwd()


# Default storage path:
#   <project_root>/storage/attachments
_DEFAULT_ATTACHMENTS_ROOT = _PROJECT_ROOT / "storage" / "attachments"


def get_attachments_root() -> Path:
    """
    Resolve the attachments root directory.

    Precedence:
    1) MLT_ATTACHMENTS_ROOT environment variable
    2) <project_root>/storage/attachments

    Ensures the directory exists.
    """
    env_root = os.getenv("MLT_ATTACHMENTS_ROOT")
    if env_root:
        base = Path(env_root).expanduser().resolve()
    else:
        base = _DEFAULT_ATTACHMENTS_ROOT

    base.mkdir(parents=True, exist_ok=True)
    return base


def generate_stored_filename(original_name: str) -> str:
    """
    Generate a filesystem-safe unique filename.

    Preserves the extension if present; otherwise creates a UUID with no suffix.
    """
    suffix = Path(original_name).suffix or ""
    unique = uuid4().hex
    return f"{unique}{suffix}"


def build_storage_path(stored_name: str) -> Path:
    """
    Compute full filesystem path for a stored attachment.
    """
    root = get_attachments_root()
    return root / stored_name


def save_bytes(data: bytes, original_name: str) -> Tuple[str, str, int]:
    """
    Save raw bytes to disk.

    Returns:
        stored_name: unique filename used
        relative_path: relative path within attachments root
        file_size: number of bytes written
    """
    stored_name = generate_stored_filename(original_name)
    target_path = build_storage_path(stored_name)

    with open(target_path, "wb") as f:
        f.write(data)

    file_size = target_path.stat().st_size
    relative_path = stored_name  # same as stored_name in local FS model

    return stored_name, relative_path, file_size


def delete_file_if_exists(relative_path: str) -> None:
    """
    Delete a stored file if it exists.
    Silently ignores missing files.
    """
    if not relative_path:
        return

    target_path = get_attachments_root() / relative_path

    try:
        if target_path.exists():
            target_path.unlink()
    except OSError:
        # No raise — DB state is always the source of truth.
        pass

