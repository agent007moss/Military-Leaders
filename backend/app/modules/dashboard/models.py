# app/modules/dashboard/models.py

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Optional, Dict, Any

from sqlalchemy import (
    String,
    DateTime,
    Enum as SAEnum,
    ForeignKey,
    JSON,
    Boolean,
)
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PGUUID

from app.core.db import Base
from app.core.models_base import BaseModelMixin, Branch, Role


# ---------------------------------------------------------------------------
# MODEL: DashboardSnapshot
# ---------------------------------------------------------------------------

class DashboardSnapshot(BaseModelMixin, Base):
    """
    Stores computed summary metrics for a user.
    Cached per (user_id, unit_id, timestamp).

    metrics: Arbitrary JSON key/value structure.
    """

    __tablename__ = "dashboard_snapshots"

    user_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        index=True,
        nullable=False,
    )

    unit_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        PGUUID(as_uuid=True),
        index=True,
        nullable=True,
    )

    branch: Mapped[Optional[Branch]] = mapped_column(
        SAEnum(Branch, name="branch_enum"),
        nullable=True,
    )

    role: Mapped[Optional[Role]] = mapped_column(
        SAEnum(Role, name="role_enum"),
        nullable=True,
    )

    snapshot_timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    metrics: Mapped[Dict[str, Any]] = mapped_column(
        JSON,
        nullable=False,
        default=dict,
    )

    def __repr__(self) -> str:
        return f"<DashboardSnapshot id={self.id} user={self.user_id}>"


# ---------------------------------------------------------------------------
# MODEL: DashboardBoxMirror
# ---------------------------------------------------------------------------

class DashboardBoxMirror(BaseModelMixin, Base):
    """
    Per-soldier cached summary blob for each box.

    Allows extremely fast Soldier List View rendering.
    Example:
        box_name="physical_fitness"
        summary={
            "acft_score": 480,
            "last_test": "2025-01-01",
            "status_color": "GREEN",
        }
    """

    __tablename__ = "dashboard_box_mirrors"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    box_name: Mapped[str] = mapped_column(
        String(50),
        index=True,
        nullable=False,
    )

    summary: Mapped[Dict[str, Any]] = mapped_column(
        JSON,
        nullable=False,
        default=dict,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    def __repr__(self) -> str:
        return f"<DashboardBoxMirror id={self.id} soldier={self.soldier_id} box={self.box_name}>"
