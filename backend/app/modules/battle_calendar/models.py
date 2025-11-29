# app/modules/battle_calendar/models.py

from __future__ import annotations

import uuid
from datetime import date
from typing import Optional

from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models_base import BaseModel

class BattleEvent(BaseModel):
    """Minimal battle calendar event model for Phase 1 scaffold."""

    __tablename__ = "battle_events"

    service_member_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("service_members.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(String(200), nullable=False)
    start_date: Mapped[Optional[date]] = mapped_column(Date)
    end_date: Mapped[Optional[date]] = mapped_column(Date)
    location: Mapped[Optional[str]] = mapped_column(String(200))
    notes: Mapped[Optional[str]] = mapped_column(String(500))

    service_member = relationship("ServiceMember", backref="battle_events")
