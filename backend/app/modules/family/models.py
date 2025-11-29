# app/modules/family/models.py

from __future__ import annotations

import uuid
from typing import Optional

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models_base import BaseModel

class FamilyMember(BaseModel):
    """Basic family member record linked to a service member."""

    __tablename__ = "family_members"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    relationship_type: Mapped[Optional[str]] = mapped_column(String(50))
    first_name: Mapped[Optional[str]] = mapped_column(String(100))
    last_name: Mapped[Optional[str]] = mapped_column(String(100))
    phone: Mapped[Optional[str]] = mapped_column(String(32))
    notes: Mapped[Optional[str]] = mapped_column(String(500))

    service_member = relationship("ServiceMember", backref="family_members")
