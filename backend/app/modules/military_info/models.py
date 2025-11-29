# app/modules/military_info/models.py

from __future__ import annotations

import uuid
from typing import Optional

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models_base import BaseModel

class ServiceMemberMilitaryInfo(BaseModel):
    """Aggregated branch-specific military info shell."""

    __tablename__ = "service_member_military_info"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
        index=True,
    )

    branch_summary: Mapped[Optional[str]] = mapped_column(String(500))

    service_member = relationship("ServiceMember", backref="military_info")
