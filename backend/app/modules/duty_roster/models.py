# app/modules/duty_roster/models.py

from __future__ import annotations

import uuid
from datetime import date
from typing import Optional

from sqlalchemy import (
    String,
    Date,
    ForeignKey,
    Enum as SAEnum,
    Boolean,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PGUUID

from app.core.db import Base
from app.core.models_base import BaseModelMixin


# ---------------------------------------------------------------------------
# MODEL: StatusCategory
# ---------------------------------------------------------------------------

class StatusCategory(BaseModelMixin, Base):
    """
    Defines a duty roster status category:
        - Leave
        - Quarters
        - PDY
        - TDY
        - Field
        - Mission
        - Admin-defined categories
    """

    __tablename__ = "duty_status_categories"

    name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    description: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )

    is_default: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )


# ---------------------------------------------------------------------------
# MODEL: DailyStatus
# ---------------------------------------------------------------------------

class DailyStatus(BaseModelMixin, Base):
    """
    One soldier's personnel status for a specific date.

    Required:
        - soldier_id
        - date
        - status_category_id
    """

    __tablename__ = "duty_daily_status"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    date: Mapped[date] = mapped_column(
        Date,
        index=True,
        nullable=False,
    )

    status_category_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("duty_status_categories.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    notes: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )

    # Relationship to category
    category: Mapped[StatusCategory] = relationship("StatusCategory")
