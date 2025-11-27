"""Database placeholder.

Phase 1 skeleton intentionally does NOT implement any database connection.
This module exposes stub functions/types so other modules can import them
without failing, to be replaced with real infrastructure later.
"""

from typing import Any


class SessionPlaceholder:
    """Non-functional stand‑in for a DB session object."""

    def __getattr__(self, name: str) -> Any:  # pragma: no cover - placeholder
        raise RuntimeError("Database layer not implemented in Phase 1 skeleton")


def get_db() -> SessionPlaceholder:
    """Dependency stub for future DB session injection."""
    return SessionPlaceholder()
