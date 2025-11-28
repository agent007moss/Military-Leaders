# app/modules/hr_metrics/models.py

from __future__ import annotations

import enum
import uuid
from datetime import date
from typing import Optional

from sqlalchemy import (
    String,
    Date,
    Integer,
    Boolean,
    Text,
    ForeignKey,
    Enum as SAEnum,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from app.core.models_base import BaseModel, Branch
from app.modules.soldier_profile.models import ServiceMember  # Needed for SA2.0 typing


# ---------------------------------------------------------------------------
# ENUMS
# ---------------------------------------------------------------------------

class HRMetricKind(str, enum.Enum):
    PHA = "PHA"
    SGLI = "SGLI"
    EMERGENCY_DATA = "EMERGENCY_DATA"
    RECORDS_REVIEW = "RECORDS_REVIEW"
    CUSTOM = "CUSTOM"


class HRMetricStatusColor(str, enum.Enum):
    GREEN = "GREEN"
    AMBER = "AMBER"
    RED = "RED"
    NEUTRAL = "NEUTRAL"


# ---------------------------------------------------------------------------
# METRIC DEFINITION TABLE
# ---------------------------------------------------------------------------

class HRMetricDefinition(BaseModel):
    """
    Per-branch HR metric metadata.
    """

    __tablename__ = "hr_metric_definitions"

    branch: Mapped[Optional[Branch]] = mapped_column(
        SAEnum(Branch, name="branch_enum", inherit_schema=True),
        nullable=True,
        index=True,
    )

    kind: Mapped[HRMetricKind] = mapped_column(
        SAEnum(HRMetricKind, name="hr_metric_kind_enum", inherit_schema=True),
        nullable=False,
    )

    key: Mapped[str] = mapped_column(String(64), nullable=False)
    display_name: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)

    default_expiration_days: Mapped[int] = mapped_column(Integer, default=365)

    green_threshold_days: Mapped[int] = mapped_column(Integer, default=90)
    amber_threshold_days: Mapped[int] = mapped_column(Integer, default=30)

    is_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    is_required: Mapped[bool] = mapped_column(Boolean, default=False)
    notifications_enabled: Mapped[bool] = mapped_column(Boolean, default=True)

    entries: Mapped[list["HRMetricEntry"]] = relationship(
        "HRMetricEntry",
        back_populates="definition",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        UniqueConstraint("branch", "key", name="uq_hr_metric_def_branch_key"),
    )

    def __repr__(self) -> str:
        branch_value = self.branch.value if self.branch else "GLOBAL"
        return f"<HRMetricDefinition id={self.id} branch={branch_value} key={self.key}>"


# ---------------------------------------------------------------------------
# METRIC ENTRY TABLE
# ---------------------------------------------------------------------------

class HRMetricEntry(BaseModel):
    """
    Actual recorded HR metric for a ServiceMember.
    """

    __tablename__ = "hr_metric_entries"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    definition_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("hr_metric_definitions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    date_completed: Mapped[date] = mapped_column(Date, nullable=False)
    expiration_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)

    status_color: Mapped[HRMetricStatusColor] = mapped_column(
        SAEnum(HRMetricStatusColor, name="hr_metric_status_color_enum", inherit_schema=True),
        nullable=False,
        default=HRMetricStatusColor.GREEN,
    )

    notifications_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    notes: Mapped[Optional[str]] = mapped_column(Text)

    definition: Mapped[HRMetricDefinition] = relationship(
        "HRMetricDefinition",
        back_populates="entries",
    )

    service_member: Mapped[ServiceMember] = relationship(
        ServiceMember,
        backref="hr_metric_entries",
    )

    __table_args__ = ()  # Correct, empty tuple

    def __repr__(self) -> str:
        return (
            f"<HRMetricEntry id={self.id} sm={self.service_member_id} "
            f"def={self.definition_id} status={self.status_color.value}>"
        )

