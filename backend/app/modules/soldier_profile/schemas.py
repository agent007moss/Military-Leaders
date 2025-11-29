from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from app.core.models_base import Branch, Component


class ServiceMemberCreate(BaseModel):
    first_name: str
    last_name: str
    middle_initial: Optional[str] = None
    branch: Branch
    component: Optional[Component] = None
    owner_user_id: Optional[UUID] = None


class ServiceMemberRead(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    middle_initial: Optional[str] = None
    branch: Branch
    component: Optional[Component] = None
    owner_user_id: Optional[UUID] = None

    class Config:
        from_attributes = True
