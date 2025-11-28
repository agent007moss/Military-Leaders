# app/modules/flags_ucmj/models.py

from __future__ import annotations

import uuid
from datetime import date
from typing import Optional

from sqlalchemy import (
    String,
    Date,
    Boolean,
    ForeignKey,
    Index,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models_base import BaseModel
from app.modules.soldier_profile.models import ServiceMember


# ---------------------------------------------------------------------------
# MODEL: FlagAction
# ---------------------------------------------------------------------------

class FlagAction(BaseModel):
    """
    Unified model for Flags, Adverse Actions, UCMJ Actions,
    Legal Holds, Command Holds, and all branch-specific equivalents.
    """

    __tablename__ = "flag_actions"

    # --------------------------------------------------------
    # Foreign Key
    # --------------------------------------------------------
    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # --------------------------------------------------------
    # Core Fields
    # --------------------------------------------------------
    category: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
        index=True,
        comment="Admin-defined category: Flag, Legal Hold, Article 15, etc.",
    )

    auto_title: Mapped[str] = mapped_column(
        String(256),
        nullable=False,
        comment="Auto-generated cached title: 'Category Rank Last YYYY MMM DD'.",
    )

    start_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)

    expiration_date: Mapped[Optional[date]] = mapped_column(
        Date,
        nullable=True,
        comment="Optional expiration. When null → status NEUTRAL.",
    )

    status_color: Mapped[Optional[str]] = mapped_column(
        String(16),
        nullable=True,
        comment="GREEN / AMBER / RED / GRAY / NEUTRAL. Computed externally.",
    )

    notes: Mapped[Optional[str]] = mapped_column(String(2048), nullable=True)

    closed_out: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        comment="True when resolved. Entry becomes read-only.",
    )

    # ORM relationship
    service_member: Mapped[ServiceMember] = relationship(
        ServiceMember,
        backref="flag_actions",
        lazy="selectin",
    )

    __table_args__ = (
        Index("ix_flagactions_member_date", "service_member_id", "start_date"),
    )

    def __repr__(self) -> str:
        return f"<FlagAction id={self.id} member={self.service_member_id} cat={self.category}>"


# ---------------------------------------------------------------------------
# MODEL: FlagActionAttachment
# ---------------------------------------------------------------------------

class FlagActionAttachment(BaseModel):
    """
    Attachments for any Flag/UCMJ action: Article 15, GOMOR, legal docs, etc.
    """

    __tablename__ = "flag_action_attachments"

    flag_action_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("flag_actions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    file_path: Mapped[str] = mapped_column(
        String(512),
        nullable=False,
        comment="File system or S3 path",
    )

    description: Mapped[Optional[str]] = mapped_column(
        String(256),
        nullable=True,
    )

    flag_action: Mapped[FlagAction] = relationship(
        FlagAction,
        backref="attachments",
        lazy="selectin",
    )

    def __repr__(self) -> str:
        return f"<FlagActionAttachment id={self.id} file={self.file_path}>"

