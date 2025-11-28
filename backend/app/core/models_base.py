# app/core/models_base.py

import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, Boolean, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import declared_attr
from enum import Enum
from .db import Base

# ================================================================
# ENUM DEFINITIONS
# ================================================================
class Branch(str, Enum):
    ARMY = "Army"
    MARINES = "Marines"
    NAVY = "Navy"
    AIR_FORCE = "AirForce"
    SPACE_FORCE = "SpaceForce"
    COAST_GUARD = "CoastGuard"


class Component(str, Enum):
    ACTIVE = "Active"
    RESERVE = "Reserve"
    GUARD = "Guard"
    OTHER = "Other"


class Role(str, Enum):
    OWNER_DEVELOPER_ADMIN = "OwnerDeveloperAdmin"
    SUPPORT_ADMIN = "SupportAdmin"
    UNIT_ADMIN = "UnitAdmin"
    STANDARD_USER = "StandardUser"


# ================================================================
# BASE MODEL MIXIN
# ================================================================
class BaseModelMixin:
    """Shared fields for all models."""

    id = Column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    is_deleted = Column(
        Boolean,
        nullable=False,
        default=False
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


# ================================================================
# BASE CLASS FOR ALL MODELS
# ================================================================
class BaseModel(Base, BaseModelMixin):
    """
    All models inherit from BaseModel.
    Mixin handles common columns.
    """
    __abstract__ = True

