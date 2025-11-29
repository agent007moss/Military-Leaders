# app/modules/licenses/models.py

from __future__ import annotations

import uuid
from datetime import date
from typing import Optional

from sqlalchemy import String, Date, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models_base import BaseModel

class LicenseRecord(BaseModel):
    """Basic driver/license tracking record."""

    __tablename__ = "license_records"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    license_type: Mapped[str] = mapped_column(String(50), nullable=False)
    identifier: Mapped[Optional[str]] = mapped_column(String(100))
    issue_date: Mapped[Optional[date]] = mapped_column(Date)
    expiration_date: Mapped[Optional[date]] = mapped_column(Date)
    is_military: Mapped[bool] = mapped_column(Boolean, default=False)

    service_member = relationship("ServiceMember", backref="license_records")
