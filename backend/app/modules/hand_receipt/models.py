# app/modules/hand_receipt/models.py

from __future__ import annotations

import enum
import uuid
from datetime import date
from typing import Optional

from sqlalchemy import (
    Boolean,
    Date,
    Enum as SAEnum,
    ForeignKey,
    Text,
    String,
)
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base
from app.core.models_base import BaseModelMixin


# -------------------------------------------------------
# ENUMS
# -------------------------------------------------------

class ItemCategory(str, enum.Enum):
    """
    Universal + branch-specific equipment categories.
    Admins may override names in metadata later.
    """
    VEHICLE = "VEHICLE"
    WEAPON_ACCESSORY = "WEAPON_ACCESSORY"
    COMMS = "COMMS"
    TOOLS = "TOOLS"
    ENGINEERING = "ENGINEERING"
    KEYS = "KEYS"
    ROOMS = "ROOMS"
    TRAINING = "TRAINING"
    SENSITIVE = "SENSITIVE"
    OFFICE = "OFFICE"
    OTHER = "OTHER"


class ItemCondition(str, enum.Enum):
    """
    Standard condition codes for both Hand Receipts and
    Equipment Responsibility modules.
    """
    NEW = "NEW"
    EXCELLENT = "EXCELLENT"
    GOOD = "GOOD"
    FAIR = "FAIR"
    DAMAGED = "DAMAGED"
    NEEDS_REPAIR = "NEEDS_REPAIR"
    MISSING_PARTS = "MISSING_PARTS"
    UNSERVICEABLE = "UNSERVICEABLE"


# -------------------------------------------------------
# MODEL: HandReceiptItem
# -------------------------------------------------------

class HandReceiptItem(BaseModelMixin, Base):
    """
    Represents a single issued item for a soldier.

    Serial enforcement, sensitive item rules, and attachment
    validation will be implemented in service logic.
    """

    __tablename__ = "hand_receipt_items"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    category: Mapped[ItemCategory] = mapped_column(
        SAEnum(ItemCategory, name="hand_receipt_category_enum"),
        nullable=False,
    )

    item_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    serial_number: Mapped[Optional[str]] = mapped_column(
        String(120),
        nullable=True,
    )

    sub_hand_receipt_number: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
    )

    date_issued: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    date_returned: Mapped[Optional[date]] = mapped_column(
        Date,
        nullable=True,
    )

    issued_by_rank: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    issued_by_last: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    issued_by_first: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    issued_by_phone: Mapped[Optional[str]] = mapped_column(
        String(25),
        nullable=True,
    )

    condition: Mapped[ItemCondition] = mapped_column(
        SAEnum(ItemCondition, name="hand_receipt_condition_enum"),
        nullable=False,
    )

    is_returned: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    notes: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    # Placeholder for Phase 2 attachment system
    attachment_refs: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    def __repr__(self) -> str:
        return (
            f"<HandReceiptItem id={self.id} soldier={self.soldier_id} "
            f"name={self.item_name!r} returned={self.is_returned}>"
        )
