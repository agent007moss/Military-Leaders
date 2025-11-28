# app/modules/equipment_responsible/__init__.py

"""
Equipment Responsible For module.

Exports:
- EquipmentResponsibleEntry
- EquipmentCategory
- ResponsibilityType
- ItemCondition
- EquipmentStatus

Provides Phase A get_router() stub.
"""

from .models import (
    EquipmentResponsibleEntry,
    EquipmentCategory,
    ResponsibilityType,
    ItemCondition,
    EquipmentStatus,
)

__all__ = [
    "EquipmentResponsibleEntry",
    "EquipmentCategory",
    "ResponsibilityType",
    "ItemCondition",
    "EquipmentStatus",
]


def get_router():
    """
    Phase A stub router (no endpoints yet).
    Ensures compatibility with app/core/router.py.
    """
    from fastapi import APIRouter

    router = APIRouter(
        prefix="/equipment-responsible",
        tags=["equipment_responsible"],
    )
    return router
