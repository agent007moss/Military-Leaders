# app/modules/rating_scheme/__init__.py

"""
Rating Scheme module.

Exports:
- RatingSchemeEntry
- RatingRole
- RatingSchemeStatus

Provides a Phase A get_router() stub so the module loads cleanly.
"""

from .models import (
    RatingSchemeEntry,
    RatingRole,
    RatingSchemeStatus,
)

__all__ = [
    "RatingSchemeEntry",
    "RatingRole",
    "RatingSchemeStatus",
]


def get_router():
    """
    Phase A stub router (no endpoints yet).
    Allows app/core/router.py to import this module without failure.
    """
    from fastapi import APIRouter

    router = APIRouter(
        prefix="/rating-scheme",
        tags=["rating_scheme"],
    )
    return router
