# app/modules/auth/schemas.py

from __future__ import annotations
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
    role: Role   # will return Enum automatically

    model_config = {
        "from_attributes": True
    }
