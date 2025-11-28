# app/modules/tasks/__init__.py

"""
Tasking module.

Exposes ORM models for:
- TaskEntry
- TaskType
- TaskStatusColor

Routers and service logic will be implemented in later phases.
"""

from .models import (
    TaskEntry,
    TaskType,
    TaskStatusColor,
)

__all__ = [
    "TaskEntry",
    "TaskType",
    "TaskStatusColor",
]


def get_router():
    """
    Minimal router stub so the module loads cleanly
    during Phase A (models-only).
    """
    from fastapi import APIRouter

    router = APIRouter(
        prefix="/tasks",
        tags=["tasks"],
    )
    return router
