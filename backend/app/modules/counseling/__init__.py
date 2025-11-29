# app/modules/counseling/__init__.py

"""
Counseling Module (Phase A)

Exports:
- CounselingType
- CounselingEntry

Provides a Phase A router stub for integration with app/core/router.py.
"""

from .models import (
    CounselingType,
    CounselingEntry,
)

__all__ = [
    "CounselingType",
    "CounselingEntry",
]


def get_router():
    """
    Phase A stub router.
    Actual endpoints added in API phase.
    """
    from fastapi import APIRouter

    router = APIRouter(
        prefix="/counseling",
        tags=["counseling"],
    )
    return router
