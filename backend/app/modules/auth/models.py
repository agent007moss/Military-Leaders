# app/modules/auth/models.py

from __future__ import annotations
import uuid
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from app.core.models_base import BaseModel, Role


class UserAccount(BaseModel):
    __tablename__ = "user_accounts"

    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    # store ENUM as pure string
    role: Mapped[str] = mapped_column(
        String(50),
        default=Role.StandardUser.value,     # must use string value
        nullable=False,
    )
