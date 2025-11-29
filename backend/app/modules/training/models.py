# app/modules/training/models.py
from __future__ import annotations

import enum
import uuid
from datetime import date
from typing import Optional

from sqlalchemy import (
    String,
    Date,
    Boolean,
    Text,
    Enum as SAEnum,
    ForeignKey,
    Integer,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PGUUID

from app.core.db import Base
from app.core.models_base import BaseModelMixin


# ---------------------------------------------------------------------------
# ENUMS
# ---------------------------------------------------------------------------

class TrainingStatusColor(str, enum.Enum):
    GREEN = "GREEN"
    AMBER = "AMBER"
    RED = "RED"
    EXPIRED = "EXPIRED"
    NEUTRAL = "NEUTRAL"


# ---------------------------------------------------------------------------
# MODEL
# ---------------------------------------------------------------------------

class TrainingEntry(BaseModelMixin, Base):
    """
    Stores one training record for a Soldier.
    """

    __tablename__ = "training_entries"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    training_type: Mapped[str] = mapped_column(String(200), index=True)

    training_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)

    expiration_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)

    is_required: Mapped[bool] = mapped_column(Boolean, default=False)

    status_color: Mapped[Optional[TrainingStatusColor]] = mapped_column(
        SAEnum(TrainingStatusColor, name="training_status_color_enum"),
        nullable=True,
    )

    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    attachment_count: Mapped[int] = mapped_column(Integer, default=0)

    branch_metadata_key: Mapped[Optional[str]] = mapped_column(
        String(200),
        nullable=True,
    )


# ---------------------------------------------------------------------------
# Soldier Backref
# ---------------------------------------------------------------------------

def _attach_backref():
    """Bind relationship to Soldier after Soldier model is loaded."""
    from app.modules.soldier_profile.models import Soldier

    if not hasattr(Soldier, "training_entries"):
        Soldier.training_entries = relationship(
            "TrainingEntry",
            backref="soldier",
            cascade="all, delete-orphan",
        )

_attach_backref()
