# app/modules/auth/models.py

from __future__ import annotations

import uuid
from datetime import datetime
from typing import List, Optional

from sqlalchemy import (
    String,
    Boolean,
    DateTime,
    Enum as SAEnum,
    ForeignKey,
    UniqueConstraint,
    Index,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.db import Base
from app.core.models_base import BaseModel, Branch, Component, Role


class UserAccount(BaseModel):
    """
    Global user account for login and high-level role.
    Per-unit roles are stored in UnitMembership.
    """

    __tablename__ = "user_accounts"

    # Authentication core
    email: Mapped[str] = mapped_column(
        String(320),
        nullable=False,
        unique=True,
        index=True,
    )
    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    # Display / identity
    first_name: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
    )
    last_name: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )
    display_name: Mapped[Optional[str]] = mapped_column(
        String(150),
        nullable=True,
    )

    # Global role
    global_role: Mapped[Role] = mapped_column(
        SAEnum(Role, name="role_enum"),
        nullable=False,
        default=Role.STANDARD_USER,
    )

    # Optional defaults
    default_branch: Mapped[Optional[Branch]] = mapped_column(
        SAEnum(Branch, name="branch_enum"),
        nullable=True,
    )
    default_component: Mapped[Optional[Component]] = mapped_column(
        SAEnum(Component, name="component_enum"),
        nullable=True,
    )

    # State / audit
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )
    is_locked: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )
    last_login_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime,
        nullable=True,
    )

    # Relationships
    memberships: Mapped[List["UnitMembership"]] = relationship(
        "UnitMembership",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    def __repr__(self) -> str:
        return f"<UserAccount id={self.id} email={self.email!r} active={self.is_active}>"

    __table_args__ = (
        Index("ix_user_accounts_last_name", "last_name"),
    )


class Unit(BaseModel):
    """
    Military unit or organization.
    """

    __tablename__ = "units"

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    branch: Mapped[Branch] = mapped_column(
        SAEnum(Branch, name="branch_enum", inherit_schema=True),
        nullable=False,
    )
    component: Mapped[Optional[Component]] = mapped_column(
        SAEnum(Component, name="component_enum", inherit_schema=True),
        nullable=True,
    )

    external_code: Mapped[Optional[str]] = mapped_column(
        String(32),
        nullable=True,
        index=True,
    )

    # Hierarchy (optional parent unit)
    parent_unit_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("units.id", ondelete="SET NULL"),
        nullable=True,
    )

    # Relationships
    parent_unit: Mapped[Optional["Unit"]] = relationship(
        "Unit",
        remote_side="Unit.id",
        backref="child_units",
        lazy="selectin",
    )

    memberships: Mapped[List["UnitMembership"]] = relationship(
        "UnitMembership",
        back_populates="unit",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    def __repr__(self) -> str:
        return f"<Unit id={self.id} name={self.name!r} branch={self.branch.value}>"


class UnitMembership(BaseModel):
    """
    Links a user to a unit with a specific role within that unit.
    """

    __tablename__ = "unit_memberships"

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("user_accounts.id", ondelete="CASCADE"),
        nullable=False,
    )
    unit_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("units.id", ondelete="CASCADE"),
        nullable=False,
    )

    role: Mapped[Role] = mapped_column(
        SAEnum(Role, name="role_enum", inherit_schema=True),
        nullable=False,
        default=Role.STANDARD_USER,
    )

    is_primary_unit: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    # Relationships
    user: Mapped[UserAccount] = relationship(
        "UserAccount",
        back_populates="memberships",
        lazy="joined",
    )
    unit: Mapped[Unit] = relationship(
        "Unit",
        back_populates="memberships",
        lazy="joined",
    )

    def __repr__(self) -> str:
        return (
            f"<UnitMembership id={self.id} user_id={self.user_id} "
            f"unit_id={self.unit_id} role={self.role.value}>"
        )

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "unit_id",
            name="uq_unit_memberships_user_unit",
        ),
        Index(
            "ix_unit_memberships_unit_role",
            "unit_id",
            "role",
        ),
    )

