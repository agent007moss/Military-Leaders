"""
PERSTATS Module (Phase A Models Only)

Exports:
- PerstatsEntry
"""

from .models import PerstatsEntry

__all__ = [
    "PerstatsEntry",
]


def get_router():
    """
    Phase A stub router.
    Real endpoints arrive during API implementation phase.
    """
    from fastapi import APIRouter

    router = APIRouter(
        prefix="/perstats",
        tags=["perstats"],
    )
    return router
