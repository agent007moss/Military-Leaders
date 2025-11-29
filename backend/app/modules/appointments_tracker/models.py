# app/modules/appointments_tracker/models.py

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models_base import BaseModel

class AppointmentEntry(BaseModel):
    """General-purpose appointment tracker entry."""

    __tablename__ = "appointment_entries"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    category: Mapped[Optional[str]] = mapped_column(String(50))
    description: Mapped[Optional[str]] = mapped_column(String(200))
    start_time: Mapped[Optional[datetime]] = mapped_column(DateTime)
    end_time: Mapped[Optional[datetime]] = mapped_column(DateTime)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)

    service_member = relationship("ServiceMember", backref="appointment_entries")
