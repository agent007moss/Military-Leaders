"""API schema placeholders for `physical_fitness`.

Define request/response DTOs here in later implementation phases.
"""

from pydantic import BaseModel, Field
from typing import Dict, Any


class PhysicalFitnessCreate(BaseModel):
    """Minimal create schema placeholder."""

    data: Dict[str, Any] = Field(default_factory=dict)


class PhysicalFitnessRead(BaseModel):
    """Minimal read schema placeholder."""

    id: str
    data: Dict[str, Any]
