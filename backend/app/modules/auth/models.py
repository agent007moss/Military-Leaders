from __future__ import annotations

from typing import Optional

from sqlalchemy import String, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models_base import BaseModel, Role


class UserAccount(BaseModel):
    __tablename__ = "user_accounts"

    username: Mapped[str] = mapped_column(String(150), unique=True, nullable=False, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    role: Mapped[Role] = mapped_column(
        SAEnum(Role, name="role_enum"),
        nullable=False,
        default=Role.StandardUser,
    )

    display_name: Mapped[Optional[str]] = mapped_column(String(255))
