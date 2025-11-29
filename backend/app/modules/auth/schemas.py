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
    role: Role

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    username_or_email: str
    password: str


class RefreshRequest(BaseModel):
    refresh_token: str


class TokenPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
