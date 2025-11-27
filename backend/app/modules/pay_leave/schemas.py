"""API schema placeholders for `pay_leave`.

Define request/response DTOs here in later implementation phases.
"""

from pydantic import BaseModel, Field
from typing import Dict, Any


class PayLeaveCreate(BaseModel):
    """Minimal create schema placeholder."""

    data: Dict[str, Any] = Field(default_factory=dict)


class PayLeaveRead(BaseModel):
    """Minimal read schema placeholder."""

    id: str
    data: Dict[str, Any]
