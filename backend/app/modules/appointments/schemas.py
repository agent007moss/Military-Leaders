"""API schema placeholders for `appointments`.

Define request/response DTOs here in later implementation phases.
"""

from pydantic import BaseModel, Field
from typing import Dict, Any


class AppointmentsCreate(BaseModel):
    """Minimal create schema placeholder."""

    data: Dict[str, Any] = Field(default_factory=dict)


class AppointmentsRead(BaseModel):
    """Minimal read schema placeholder."""

    id: str
    data: Dict[str, Any]
