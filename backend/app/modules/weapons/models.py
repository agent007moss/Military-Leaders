# app/modules/weapons/models.py

from __future__ import annotations

import uuid
from datetime import date
from typing import Optional

from sqlalchemy import String, Date, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models_base import BaseModel

class WeaponQualification(BaseModel):
    """Minimal weapons qualification record."""

    __tablename__ = "weapon_qualifications"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    weapon_type: Mapped[str] = mapped_column(String(50), nullable=False)
    qual_date: Mapped[Optional[date]] = mapped_column(Date)
    expiration_date: Mapped[Optional[date]] = mapped_column(Date)
    passed: Mapped[bool] = mapped_column(Boolean, default=True)
    score: Mapped[Optional[str]] = mapped_column(String(50))

    service_member = relationship("ServiceMember", backref="weapon_qualifications")
