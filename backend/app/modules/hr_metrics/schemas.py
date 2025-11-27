"""API schema placeholders for `hr_metrics`.

Define request/response DTOs here in later implementation phases.
"""

from pydantic import BaseModel, Field
from typing import Dict, Any


class HrMetricsCreate(BaseModel):
    """Minimal create schema placeholder."""

    data: Dict[str, Any] = Field(default_factory=dict)


class HrMetricsRead(BaseModel):
    """Minimal read schema placeholder."""

    id: str
    data: Dict[str, Any]
