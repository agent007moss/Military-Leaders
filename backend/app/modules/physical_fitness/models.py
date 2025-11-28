# app/modules/physical_fitness/models.py

from __future__ import annotations

import uuid
from datetime import date
from typing import Optional
from enum import Enum

from sqlalchemy import (
    String,
    Date,
    Integer,
    Boolean,
    ForeignKey,
    Enum as SAEnum,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models_base import BaseModel, Branch
from app.modules.soldier_profile.models import ServiceMember


# ============================================================
# ENUMS
# ============================================================

class FitnessTestType(str, Enum):
    ARMY_AFT = "ARMY_AFT"
    MARINE_PFT = "MARINE_PFT"
    MARINE_CFT = "MARINE_CFT"
    NAVY_PRT = "NAVY_PRT"
    AIR_FORCE_FA = "AIR_FORCE_FA"
    SPACE_FORCE_FA = "SPACE_FORCE_FA"
    COAST_GUARD_PFT = "COAST_GUARD_PFT"


class FitnessStatusColor(str, Enum):
    GREEN = "GREEN"
    AMBER = "AMBER"
    RED = "RED"
    GRAY = "GRAY"


# ============================================================
# MODEL: PhysicalFitnessTest
# ============================================================

class PhysicalFitnessTest(BaseModel):
    """
    Universal fitness test object.
    Contains core fields only. Scoring and expiration logic is handled
    later in service-layer implementations.
    """

    __tablename__ = "physical_fitness_tests"

    # Relationship to ServiceMember (NOT "soldier")
    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    service_member: Mapped[ServiceMember] = relationship(
        ServiceMember,
        backref="fitness_tests",
        lazy="selectin",
    )

    # Branch → determines valid test types
    branch: Mapped[Branch] = mapped_column(
        SAEnum(Branch, name="branch_enum", inherit_schema=True),
        nullable=False,
        index=True,
    )

    # Test metadata
    test_type: Mapped[FitnessTestType] = mapped_column(
        SAEnum(FitnessTestType, name="fitness_test_type_enum", inherit_schema=True),
        nullable=False,
    )

    test_date: Mapped[date] = mapped_column(Date, nullable=False)

    # Stored expiration (computed later)
    expiration_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)

    # Stored color (computed later)
    status_color: Mapped[Optional[FitnessStatusColor]] = mapped_column(
        SAEnum(FitnessStatusColor, name="fitness_status_color_enum", inherit_schema=True),
        nullable=True,
    )

    # Scoring
    total_score: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    passed: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)

    # Notes
    notes: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    def __repr__(self) -> str:
        return (
            f"<PhysicalFitnessTest id={self.id} sm={self.service_member_id} "
            f"type={self.test_type.value} date={self.test_date}>"
        )

