# app/modules/evaluations/models.py

from __future__ import annotations

import enum
import uuid
from datetime import date
from typing import Optional

from sqlalchemy import (
    Date,
    Enum as SAEnum,
    Text,
    String,
    Boolean,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base
    # BaseModelMixin gives: id, created_at, updated_at, is_deleted, __tablename__
from app.core.models_base import BaseModelMixin


# ---------------------------------------------------------------------------
# ENUMS
# ---------------------------------------------------------------------------

class EvaluationType(str, enum.Enum):
    """
    Universal baseline evaluation types.
    """
    NCOER_ANNUAL = "NCOER_ANNUAL"
    NCOER_COR = "NCOER_COR"
    NCOER_RFC = "NCOER_RFC"
    NCOER_CTR = "NCOER_COMPLETE_THE_RECORD"

    OER_ANNUAL = "OER_ANNUAL"
    OER_COR = "OER_COR"
    OER_RFC = "OER_RFC"
    OER_CTR = "OER_COMPLETE_THE_RECORD"

    SUPPORT_FORM = "SUPPORT_FORM"
    INITIAL_COUNSELING = "INITIAL_COUNSELING"

    OTHER = "OTHER"


class EvaluationApprovalStatus(str, enum.Enum):
    """
    Standard evaluation workflow.
    """
    DRAFT = "DRAFT"
    RATER_REVIEWING = "RATER_REVIEWING"
    SENIOR_RATER_REVIEWING = "SENIOR_RATER_REVIEWING"
    CORRECTIONS_NEEDED = "CORRECTIONS_NEEDED"
    SUBMITTED = "SUBMITTED"
    APPROVED = "APPROVED"
    FILED = "FILED"
    RETURNED = "RETURNED"
    DISAPPROVED = "DISAPPROVED"


class EvaluationStatusColor(str, enum.Enum):
    """
    Suspense-driven color states.
    """
    GREEN = "GREEN"
    AMBER = "AMBER"
    RED = "RED"
    GRAY = "GRAY"
    NONE = "NONE"


# ---------------------------------------------------------------------------
# MODEL
# ---------------------------------------------------------------------------

class EvaluationEntry(BaseModelMixin, Base):
    """
    Stores one evaluation record for a Soldier.
    Title auto-generated in service layer:
        "<EvalType> <Rank> <Last> <DDMMMYYYY>"
    """

    __tablename__ = "evaluation_entries"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    # Pre-computed title for easy list display
    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    evaluation_type: Mapped[EvaluationType] = mapped_column(
        SAEnum(EvaluationType, name="evaluation_type_enum"),
        nullable=False,
    )

    # Evaluation period (optional in some cases)
    period_start: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    period_end: Mapped[Optional[date]] = mapped_column(Date, nullable=True)

    # Event dates
    evaluation_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )
    suspense_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    status_color: Mapped[EvaluationStatusColor] = mapped_column(
        SAEnum(EvaluationStatusColor, name="evaluation_status_color_enum"),
        nullable=False,
        default=EvaluationStatusColor.NONE,
    )

    approval_status: Mapped[EvaluationApprovalStatus] = mapped_column(
        SAEnum(EvaluationApprovalStatus, name="evaluation_approval_status_enum"),
        nullable=False,
        default=EvaluationApprovalStatus.DRAFT,
    )

    completed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    # Attachments (Phase 2)
    attachment_refs: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    notes: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    def __repr__(self) -> str:
        return (
            f"<EvaluationEntry id={self.id} soldier={self.soldier_id} "
            f"type={self.evaluation_type} status={self.approval_status}>"
        )
