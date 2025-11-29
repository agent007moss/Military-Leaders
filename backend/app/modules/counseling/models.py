# app/modules/counseling/models.py

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
# MODEL: CounselingType
# ---------------------------------------------------------------------------

class CounselingType(BaseModelMixin, Base):
    """
    Defines a counseling category such as:
        - Monthly
        - Quarterly
        - Initial
        - Event-Oriented
        - Corrective Action
        - Professional Growth
    """

    __tablename__ = "counseling_types"

    name: Mapped[str] = mapped_column(
        String(80),
        unique=True,
        nullable=False,
    )

    description: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )


# ---------------------------------------------------------------------------
# MODEL: CounselingEntry
# ---------------------------------------------------------------------------

class CounselingEntry(BaseModelMixin, Base):
    """
    Stores a single counseling event for a soldier.
    """

    __tablename__ = "counseling_entries"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    counseling_type_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("counseling_types.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    counseling_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    due_date: Mapped[Optional[date]] = mapped_column(
        Date,
        nullable=True,
    )

    completed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    closed_out: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    notes: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )

    # Relationships
    counseling_type: Mapped[CounselingType] = relationship("CounselingType")
