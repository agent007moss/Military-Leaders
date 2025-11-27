"""API schema placeholders for `military_info`.

Define request/response DTOs here in later implementation phases.
"""

from pydantic import BaseModel, Field
from typing import Dict, Any


class MilitaryInfoCreate(BaseModel):
    """Minimal create schema placeholder."""

    data: Dict[str, Any] = Field(default_factory=dict)


class MilitaryInfoRead(BaseModel):
    """Minimal read schema placeholder."""

    id: str
    data: Dict[str, Any]
