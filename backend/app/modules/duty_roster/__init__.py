# app/modules/duty_roster/__init__.py

"""
Duty Roster / PERSTAT module.

Exports:
- StatusCategory
- DailyStatus

Provides a Phase A get_router() stub for core.router integration.
"""

from .models import (
    StatusCategory,
    DailyStatus,
)

__all__ = [
    "StatusCategory",
    "DailyStatus",
]


def get_router():
    """
    Phase A stub router.
    No endpoints yet — satisfies app/core/router.py requirements.
    """
    from fastapi import APIRouter

    router = APIRouter(
        prefix="/duty-roster",
        tags=["duty_roster"],
    )
    return router
