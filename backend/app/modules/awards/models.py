# app/modules/awards/models.py

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
from app.core.models_base import BaseModelMixin


# ---------------------------------------------------------------------------
# ENUMS
# ---------------------------------------------------------------------------

class AwardType(str, enum.Enum):
    """
    Universal baseline award list.
    Admins extend via metadata.
    """
    AAM = "AAM"
    ARCOM = "ARCOM"
    MSM = "MSM"
    BSM = "BSM"
    DSC = "DSC"
    MOH = "MOH"
    COA = "COA"
    LOA = "LOA"
    OTHER = "OTHER"


class AwardApprovalStatus(str, enum.Enum):
    """
    Phase 1 approval workflow.
    """
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    DISAPPROVED = "DISAPPROVED"
    RETURNED = "RETURNED"
    PRESENTED = "PRESENTED"


class AwardStatusColor(str, enum.Enum):
    """
    Optional suspense-based color coding.
    """
    GREEN = "GREEN"
    AMBER = "AMBER"
    RED = "RED"
    GRAY = "GRAY"    # closed / approved / completed
    NONE = "NONE"    # no suspense color


# ---------------------------------------------------------------------------
# MODEL: AwardEntry
# ---------------------------------------------------------------------------

class AwardEntry(BaseModelMixin, Base):
    """
    Stores a single award submission for a Soldier.

    Title will be auto-generated via service layer:
    Format: AwardType Rank LastName DDMMMYYYY or DDMMM
    """

    __tablename__ = "award_entries"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    # auto-generated title stored for listing
    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    award_type: Mapped[AwardType] = mapped_column(
        SAEnum(AwardType, name="award_type_enum"),
        nullable=False,
    )

    award_period: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    # submission + approval timeline
    date_submitted: Mapped[Optional[date]] = mapped_column(
        Date,
        nullable=True,
    )

    award_date: Mapped[Optional[date]] = mapped_column(
        Date,
        nullable=True,
    )

    suspense_date: Mapped[Optional[date]] = mapped_column(
        Date,
        nullable=True,
    )

    status_color: Mapped[AwardStatusColor] = mapped_column(
        SAEnum(AwardStatusColor, name="award_status_color_enum"),
        nullable=False,
        default=AwardStatusColor.NONE,
    )

    approval_status: Mapped[AwardApprovalStatus] = mapped_column(
        SAEnum(AwardApprovalStatus, name="award_approval_status_enum"),
        nullable=False,
        default=AwardApprovalStatus.DRAFT,
    )

    # attachments placeholder for Phase 2
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
            f"<AwardEntry id={self.id} soldier={self.soldier_id} "
            f"type={self.award_type} status={self.approval_status}>"
        )
