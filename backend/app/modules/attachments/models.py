# app/modules/attachments/models.py

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models_base import BaseModel


class Attachment(BaseModel):
    """
    Generic attachment record using hybrid storage:
    - Files stored on disk under ../storage/attachments/
    - Database stores metadata + relative path
    """

    __tablename__ = "attachments"

    # ----------------------------------------------------
    # Generic linkage: owner object & type
    # ----------------------------------------------------
    owner_type: Mapped[Optional[str]] = mapped_column(
        String(64),
        nullable=True,
        index=True,
        doc="Logical owner domain, e.g. 'weapon_stat', 'training_event', 'counseling_entry'.",
    )

    owner_id: Mapped[Optional[str]] = mapped_column(
        String(64),
        nullable=True,
        index=True,
        doc="Opaque owner identifier (UUID string or integer string). No hard FK.",
    )

    # ----------------------------------------------------
    # File metadata
    # ----------------------------------------------------
    original_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        doc="Filename provided by client (e.g., 'orders.pdf').",
    )

    stored_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        doc="Filesystem-safe unique name (UUID + extension).",
    )

    storage_path: Mapped[str] = mapped_column(
        String(512),
        nullable=False,
        doc="Relative path under the attachments root (e.g., 'stored_name.ext').",
    )

    content_type: Mapped[Optional[str]] = mapped_column(
        String(128),
        nullable=True,
        doc="MIME type reported by client (e.g., 'application/pdf').",
    )

    file_size: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
        doc="File size in bytes.",
    )

    description: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        doc="Optional human-readable description of the attachment.",
    )

    # ----------------------------------------------------
    # Representation
    # ----------------------------------------------------
    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"<Attachment id={self.id} original_name={self.original_name!r} "
            f"owner_type={self.owner_type!r} owner_id={self.owner_id!r}>"
        )

