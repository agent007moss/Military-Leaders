# app/modules/attachments/service.py

from __future__ import annotations

import uuid
from typing import Iterable, List, Optional, Union

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Attachment
from .utils import delete_file_if_exists, save_bytes


OwnerIdType = Union[str, uuid.UUID]


# ------------------------------------------------------------
# Helper: normalize owner_id to string
# ------------------------------------------------------------
def _normalize_owner_id(owner_id: Optional[OwnerIdType]) -> Optional[str]:
    """
    Normalize owner_id to a string for storage.
    Accepts UUID instances or simple strings.
    """
    if owner_id is None:
        return None
    return str(owner_id)


# ------------------------------------------------------------
# CREATE
# ------------------------------------------------------------
def create_attachment(
    db: Session,
    *,
    data: bytes,
    original_name: str,
    content_type: Optional[str] = None,
    owner_type: Optional[str] = None,
    owner_id: Optional[OwnerIdType] = None,
    description: Optional[str] = None,
) -> Attachment:
    """
    Persist a new attachment:
      1) Save bytes to disk via hybrid storage layer.
      2) Insert metadata row into attachments table.
    """
    stored_name, relative_path, file_size = save_bytes(data, original_name)
    normalized_owner_id = _normalize_owner_id(owner_id)

    attachment = Attachment(
        owner_type=owner_type,
        owner_id=normalized_owner_id,
        original_name=original_name,
        stored_name=stored_name,
        storage_path=relative_path,
        content_type=content_type,
        file_size=file_size,
        description=description,
    )

    db.add(attachment)
    db.commit()
    db.refresh(attachment)
    return attachment


# ------------------------------------------------------------
# READ
# ------------------------------------------------------------
def get_attachment(db: Session, attachment_id: str) -> Optional[Attachment]:
    """
    Fetch a single attachment by its primary key (UUID string).
    """
    return db.get(Attachment, attachment_id)


# ------------------------------------------------------------
# LIST BY OWNER
# ------------------------------------------------------------
def list_attachments_for_owner(
    db: Session,
    *,
    owner_type: str,
    owner_id: OwnerIdType,
) -> List[Attachment]:
    """
    List all attachments for a given logical owner.
    Uses SQLAlchemy 2.0 style SELECT queries.
    """
    normalized_owner_id = _normalize_owner_id(owner_id)

    stmt = (
        select(Attachment)
        .where(
            Attachment.owner_type == owner_type,
            Attachment.owner_id == normalized_owner_id,
        )
        .order_by(Attachment.created_at.asc())
    )

    results = db.execute(stmt).scalars().all()
    return list(results)


# ------------------------------------------------------------
# DELETE SINGLE
# ------------------------------------------------------------
def delete_attachment(
    db: Session,
    attachment: Attachment,
    *,
    delete_file: bool = True,
) -> None:
    """
    Delete a single attachment row.

    If delete_file=True, also remove the stored file.
    """
    if delete_file and attachment.storage_path:
        delete_file_if_exists(attachment.storage_path)

    db.delete(attachment)
    db.commit()


# ------------------------------------------------------------
# DELETE ALL FOR OWNER
# ------------------------------------------------------------
def delete_attachments_for_owner(
    db: Session,
    *,
    owner_type: str,
    owner_id: OwnerIdType,
    delete_files: bool = True,
) -> int:
    """
    Delete all attachments associated with a given owner.

    Returns:
        number of rows deleted
    """
    attachments = list_attachments_for_owner(
        db,
        owner_type=owner_type,
        owner_id=owner_id,
    )

    count = 0
    for att in attachments:
        delete_attachment(db, att, delete_file=delete_files)
        count += 1

    return count

