"""Placeholder data models for the pay_leave module. Field sets will be defined in later phases."""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class PayLeaveModel(BaseModel):
    """Skeleton model. Replace `data` with real fields later."""
    id: str = Field(..., description="Stable identifier")
    data: Dict[str, Any] = Field(default_factory=dict, description="Placeholder field bag")
