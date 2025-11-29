from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr
from app.core.models_base import Role


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserRead(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    role: Role
    display_name: Optional[str] = None

    class Config:
        from_attributes = True
