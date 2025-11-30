from __future__ import annotations

import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


# ============================================================
# MAIN BASE MODEL (Used for user_accounts)
# ============================================================

class BaseModel(Base):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )


# ============================================================
# TABLE MIXIN FOR ALL MILITARY INFO SUBTABLES
# ============================================================

class BaseTableMixin(Base):
    """
    Simple mixin for ERB-style tables:
    - id
    - created_at
    - updated_at
    """

    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )


# ============================================================
# ENUMS
# ============================================================

class Branch(str, Enum):
    Army = "Army"
    Marines = "Marines"
    Navy = "Navy"
    AirForce = "AirForce"
    SpaceForce = "SpaceForce"
    CoastGuard = "CoastGuard"


class Component(str, Enum):
    Active = "Active"
    Reserve = "Reserve"
    NationalGuard = "NationalGuard"
    AirNationalGuard = "AirNationalGuard"


class Role(str, Enum):
    OwnerDeveloperAdmin = "OwnerDeveloperAdmin"
    SupportAdmin = "SupportAdmin"
    UnitAdmin = "UnitAdmin"
    StandardUser = "StandardUser"
