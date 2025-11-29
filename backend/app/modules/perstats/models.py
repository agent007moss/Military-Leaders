from __future__ import annotations

import uuid
from datetime import date
from typing import Optional

from sqlalchemy import (
    String,
    Date,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PGUUID

from app.core.db import Base
from app.core.models_base import BaseModelMixin


# ---------------------------------------------------------------------------
# MODEL: PerstatsEntry
# ---------------------------------------------------------------------------

class PerstatsEntry(BaseModelMixin, Base):
    """
    Phase 1 PERSTATS tracking entry.
    Tracks a Soldier's duty status for dashboard rollups.
    Multiple historical entries allowed.
    """

    __tablename__ = "perstats_entries"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("service_members.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # “PDY”, “Leave”, “Quarters”, “Recovery”, “Mission”, “Unaccounted”
    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    end_date: Mapped[Optional[date]] = mapped_column(
        Date,
        nullable=True,
    )

    notes: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )

    # active = current row for dashboard
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # stored color (“GREEN”, “AMBER”, “RED”, “GRAY”), logic in later phases
    status_color: Mapped[Optional[str]] = mapped_column(
        String(16),
        nullable=True,
    )

    service_member: Mapped["ServiceMember"] = relationship(
        back_populates="perstats_entries",
        uselist=False,
    )
