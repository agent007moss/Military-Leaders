"""API schema placeholders for `equipment_responsible`.

Define request/response DTOs here in later implementation phases.
"""

from pydantic import BaseModel, Field
from typing import Dict, Any


class EquipmentResponsibleCreate(BaseModel):
    """Minimal create schema placeholder."""

    data: Dict[str, Any] = Field(default_factory=dict)


class EquipmentResponsibleRead(BaseModel):
    """Minimal read schema placeholder."""

    id: str
    data: Dict[str, Any]
