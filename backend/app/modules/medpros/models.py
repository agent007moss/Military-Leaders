# app/modules/medpros/models.py

from __future__ import annotations

import uuid
from datetime import date
from typing import Optional

from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models_base import BaseModel

class MedprosStatus(BaseModel):
    """Minimal MEDPROS-style readiness snapshot."""

    __tablename__ = "medpros_status"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    pha_date: Mapped[Optional[date]] = mapped_column(Date)
    dental_class: Mapped[Optional[str]] = mapped_column(String(10))
    mrc: Mapped[Optional[str]] = mapped_column(String(10))
    notes: Mapped[Optional[str]] = mapped_column(String(500))

    service_member = relationship("ServiceMember", backref="medpros_entries")
