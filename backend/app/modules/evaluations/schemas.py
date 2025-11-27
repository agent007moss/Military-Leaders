"""API schema placeholders for `evaluations`.

Define request/response DTOs here in later implementation phases.
"""

from pydantic import BaseModel, Field
from typing import Dict, Any


class EvaluationsCreate(BaseModel):
    """Minimal create schema placeholder."""

    data: Dict[str, Any] = Field(default_factory=dict)


class EvaluationsRead(BaseModel):
    """Minimal read schema placeholder."""

    id: str
    data: Dict[str, Any]
