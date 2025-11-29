from __future__ import annotations

from typing import Optional
from uuid import UUID

from sqlalchemy import String, Enum as SAEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models_base import BaseModel, Branch, Component


class ServiceMember(BaseModel):
    __tablename__ = "service_members"

    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    middle_initial: Mapped[Optional[str]] = mapped_column(String(1))

    branch: Mapped[Branch] = mapped_column(
        SAEnum(Branch, name="branch_enum"),
        nullable=False,
    )
    component: Mapped[Optional[Component]] = mapped_column(
        SAEnum(Component, name="component_enum"),
        nullable=True,
    )

    owner_user_id: Mapped[Optional[UUID]] = mapped_column(
        ForeignKey("user_accounts.id", ondelete="SET NULL"),
        nullable=True,
    )

    owner: Mapped[Optional["UserAccount"]] = relationship(
        "UserAccount",
        backref="service_members",
    )
