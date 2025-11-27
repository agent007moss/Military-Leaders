"""API schema placeholders for `medical_profiles`.

Define request/response DTOs here in later implementation phases.
"""

from pydantic import BaseModel, Field
from typing import Dict, Any


class MedicalProfilesCreate(BaseModel):
    """Minimal create schema placeholder."""

    data: Dict[str, Any] = Field(default_factory=dict)


class MedicalProfilesRead(BaseModel):
    """Minimal read schema placeholder."""

    id: str
    data: Dict[str, Any]
