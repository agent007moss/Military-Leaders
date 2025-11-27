"""API schema placeholders for `flags_ucmj`.

Define request/response DTOs here in later implementation phases.
"""

from pydantic import BaseModel, Field
from typing import Dict, Any


class FlagsUcmjCreate(BaseModel):
    """Minimal create schema placeholder."""

    data: Dict[str, Any] = Field(default_factory=dict)


class FlagsUcmjRead(BaseModel):
    """Minimal read schema placeholder."""

    id: str
    data: Dict[str, Any]
