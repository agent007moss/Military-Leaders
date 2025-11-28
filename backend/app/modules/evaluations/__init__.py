# app/modules/evaluations/__init__.py

"""
Evaluations module.

Exposes:
- EvaluationEntry
- EvaluationType
- EvaluationApprovalStatus
- EvaluationStatusColor

Routers will be implemented later. This file provides a minimal
get_router() stub so the module loads cleanly during Phase A.
"""

from .models import (
    EvaluationEntry,
    EvaluationType,
    EvaluationApprovalStatus,
    EvaluationStatusColor,
)

__all__ = [
    "EvaluationEntry",
    "EvaluationType",
    "EvaluationApprovalStatus",
    "EvaluationStatusColor",
]


def get_router():
    """
    Phase A stub router.
    Prevents load-time failures in app/core/router.py.
    """
    from fastapi import APIRouter

    router = APIRouter(
        prefix="/evaluations",
        tags=["evaluations"],
    )
    return router
