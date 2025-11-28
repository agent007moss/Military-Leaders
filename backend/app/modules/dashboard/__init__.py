# app/modules/dashboard/__init__.py

"""
Dashboard module.

Exports:
- DashboardSnapshot
- DashboardBoxMirror

Includes Phase A get_router() to satisfy core.router.
"""

from .models import (
    DashboardSnapshot,
    DashboardBoxMirror,
)

__all__ = [
    "DashboardSnapshot",
    "DashboardBoxMirror",
]


def get_router():
    """
    Phase A stub router. No endpoints until API work begins.
    Ensures compatibility with app/core/router.py.
    """
    from fastapi import APIRouter

    router = APIRouter(
        prefix="/dashboard",
        tags=["dashboard"],
    )
    return router
