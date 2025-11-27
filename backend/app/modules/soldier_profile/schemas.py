"""API schema placeholders for `soldier_profile`.

Define request/response DTOs here in later implementation phases.
"""

from pydantic import BaseModel, Field
from typing import Dict, Any


class SoldierProfileCreate(BaseModel):
    """Minimal create schema placeholder."""

    data: Dict[str, Any] = Field(default_factory=dict)


class SoldierProfileRead(BaseModel):
    """Minimal read schema placeholder."""

    id: str
    data: Dict[str, Any]
