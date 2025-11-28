# app/modules/rating_scheme/models.py

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
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base
from app.core.models_base import BaseModelMixin


# ---------------------------------------------------------------------------
# ENUMS
# ---------------------------------------------------------------------------

class RatingRole(str, enum.Enum):
    """Universal baseline rating roles, admin-editable per branch."""
    RATER = "RATER"
    SENIOR_RATER = "SENIOR_RATER"
    REVIEWER = "REVIEWER"
    SUPPLEMENTARY_REVIEWER = "SUPPLEMENTARY_REVIEWER"
    ACTING_RATER = "ACTING_RATER"
    CHAIN_OF_COMMAND = "CHAIN_OF_COMMAND"
    OTHER = "OTHER"


class RatingSchemeStatus(str, enum.Enum):
    """Auto status based on end date."""
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"


# ---------------------------------------------------------------------------
# MODEL
# ---------------------------------------------------------------------------

class RatingSchemeEntry(BaseModelMixin, Base):
    """
    Stores a rating scheme entry for a Soldier.

    Auto-generated title example:
        "RATER SGT Smith 12JAN2024"
    """

    __tablename__ = "rating_scheme_entries"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    rating_role: Mapped[RatingRole] = mapped_column(
        SAEnum(RatingRole, name="rating_role_enum"),
        nullable=False,
    )

    # Rater info
    rater_rank: Mapped[str] = mapped_column(String(20), nullable=False)
    rater_last: Mapped[str] = mapped_column(String(50), nullable=False)
    rater_first: Mapped[str] = mapped_column(String(50), nullable=False)

    rater_phone: Mapped[Optional[str]] = mapped_column(String(20))
    rater_position: Mapped[Optional[str]] = mapped_column(String(100))

    # Effective dates
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[Optional[date]] = mapped_column(Date)

    status: Mapped[RatingSchemeStatus] = mapped_column(
        SAEnum(RatingSchemeStatus, name="rating_scheme_status_enum"),
        nullable=False,
        default=RatingSchemeStatus.ACTIVE,
    )

    notes: Mapped[Optional[str]] = mapped_column(Text)

    attachment_refs: Mapped[Optional[str]] = mapped_column(Text)

    def __repr__(self) -> str:
        return (
            f"<RatingSchemeEntry id={self.id} soldier={self.soldier_id} "
            f"role={self.rating_role} status={self.status}>"
        )
