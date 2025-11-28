# app/modules/equipment_responsible/models.py

from __future__ import annotations

import enum
import uuid
from datetime import date
from typing import Optional

from sqlalchemy import (
    String,
    Date,
    Text,
    Enum as SAEnum,
    ForeignKey,
)
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PGUUID

from app.core.db import Base
from app.core.models_base import BaseModelMixin


# ---------------------------------------------------------------------------
# ENUMERATIONS
# ---------------------------------------------------------------------------

class EquipmentCategory(str, enum.Enum):
    """Admin-editable base set; branch-specific metadata adds more."""
    VEHICLE = "VEHICLE"
    WEAPON_ACCESSORY = "WEAPON_ACCESSORY"
    COMMS = "COMMS"
    TOOLS = "TOOLS"
    ENGINEERING = "ENGINEERING"
    KEYS = "KEYS"
    ROOMS = "ROOMS"
    TRAINING_EQUIPMENT = "TRAINING_EQUIPMENT"
    SENSITIVE = "SENSITIVE"
    OFFICE_SUPPLY = "OFFICE_SUPPLY"
    OTHER = "OTHER"


class ResponsibilityType(str, enum.Enum):
    INDIVIDUAL = "INDIVIDUAL"
    TEAM = "TEAM"
    TEMPORARY = "TEMPORARY"
    PERMANENT = "PERMANENT"
    TURN_IN_PENDING = "TURN_IN_PENDING"
    STORAGE = "STORAGE"
    OTHER = "OTHER"


class ItemCondition(str, enum.Enum):
    NEW = "NEW"
    EXCELLENT = "EXCELLENT"
    GOOD = "GOOD"
    FAIR = "FAIR"
    DAMAGED = "DAMAGED"
    NEEDS_REPAIR = "NEEDS_REPAIR"
    MISSING_PARTS = "MISSING_PARTS"
    UNSERVICEABLE = "UNSERVICEABLE"


class EquipmentStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    RELEASED = "RELEASED"


# ---------------------------------------------------------------------------
# MODEL
# ---------------------------------------------------------------------------

class EquipmentResponsibleEntry(BaseModelMixin, Base):
    """
    Tracks equipment, keys, gear, comms, rooms, tools, and sensitive items
    that a Soldier is responsible for.
    """

    __tablename__ = "equipment_responsible_entries"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    category: Mapped[EquipmentCategory] = mapped_column(
        SAEnum(EquipmentCategory, name="equipment_category_enum"),
        nullable=False,
    )

    item_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    serial_number: Mapped[Optional[str]] = mapped_column(String(100))

    responsibility_type: Mapped[ResponsibilityType] = mapped_column(
        SAEnum(ResponsibilityType, name="responsibility_type_enum"),
        nullable=False,
    )

    date_assigned: Mapped[date] = mapped_column(Date, nullable=False)
    date_released: Mapped[Optional[date]] = mapped_column(Date)

    assigned_by_rank: Mapped[Optional[str]] = mapped_column(String(20))
    assigned_by_last: Mapped[Optional[str]] = mapped_column(String(50))
    assigned_by_first: Mapped[Optional[str]] = mapped_column(String(50))
    assigned_by_phone: Mapped[Optional[str]] = mapped_column(String(20))

    condition: Mapped[Optional[ItemCondition]] = mapped_column(
        SAEnum(ItemCondition, name="equipment_condition_enum"),
        nullable=True,
    )

    status: Mapped[EquipmentStatus] = mapped_column(
        SAEnum(EquipmentStatus, name="equipment_status_enum"),
        nullable=False,
        default=EquipmentStatus.ACTIVE,
    )

    notes: Mapped[Optional[str]] = mapped_column(Text)

    attachment_refs: Mapped[Optional[str]] = mapped_column(Text)

    def __repr__(self) -> str:
        return (
            f"<EquipmentResponsibleEntry id={self.id} soldier={self.soldier_id} "
            f"item={self.item_name} status={self.status}>"
        )
