# app/modules/awards/__init__.py

"""
Awards module.

Exposes:
- AwardEntry ORM model
- AwardType enum
- AwardApprovalStatus enum
- AwardStatusColor enum

Routers will be implemented in a later backend step.
"""

from .models import (
    AwardEntry,
    AwardType,
    AwardApprovalStatus,
    AwardStatusColor,
)

__all__ = [
    "AwardEntry",
    "AwardType",
    "AwardApprovalStatus",
    "AwardStatusColor",
]


def get_router():
    """
    Minimal router stub so the module loads cleanly.

    Required by app/core/router.py during Phase A
    (models-only backend construction).
    """
    from fastapi import APIRouter

    router = APIRouter(
        prefix="/awards",
        tags=["awards"],
    )
    return router
