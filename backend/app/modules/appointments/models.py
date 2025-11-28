# app/modules/appointments/models.py

from __future__ import annotations

import enum
import uuid
from datetime import date, time
from typing import Optional

from sqlalchemy import (
    String,
    Date,
    Time,
    Text,
    Enum as SAEnum,
    Boolean,
    ForeignKey,
    Index,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from app.core.models_base import BaseModel
from app.modules.soldier_profile.models import ServiceMember  # Required for SQLAlchemy 2.0


# ---------------------------------------------------------------------------
# ENUMS
# ---------------------------------------------------------------------------

class AppointmentStatus(str, enum.Enum):
    SCHEDULED = "SCHEDULED"
    COMPLETED = "COMPLETED"
    MISSED = "MISSED"
    NO_SHOW = "NO_SHOW"
    CANCELED = "CANCELED"


# ---------------------------------------------------------------------------
# MODEL: Appointment
# ---------------------------------------------------------------------------

class Appointment(BaseModel):
    """
    A single appointment entry for a service member.
    Stores date/time, type, location, notes, and status.
    """

    __tablename__ = "appointments"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # -----------------------------------------
    # Core Appointment Data
    # -----------------------------------------

    appointment_type: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
        index=True,
    )

    appointment_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )

    # Optional time windows
    start_time: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    end_time: Mapped[Optional[time]] = mapped_column(Time, nullable=True)

    location: Mapped[Optional[str]] = mapped_column(String(256), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text)

    # -----------------------------------------
    # Status & Notifications
    # -----------------------------------------

    status: Mapped[AppointmentStatus] = mapped_column(
        SAEnum(AppointmentStatus, name="appointment_status_enum", inherit_schema=True),
        default=AppointmentStatus.SCHEDULED,
        nullable=False,
    )

    notifications_enabled: Mapped[bool] = mapped_column(Boolean, default=True)

    # Relationship back to ServiceMember
    service_member: Mapped[ServiceMember] = relationship(
        ServiceMember,
        backref="appointments",
    )

    # -----------------------------------------
    # Calendar Optimization
    # -----------------------------------------

    __table_args__ = (
        Index(
            "ix_appointments_service_member_date",
            "service_member_id",
            "appointment_date"
        ),
    )

    def __repr__(self) -> str:
        return (
            f"<Appointment id={self.id} sm={self.service_member_id} "
            f"date={self.appointment_date} type={self.appointment_type}>"
        )

