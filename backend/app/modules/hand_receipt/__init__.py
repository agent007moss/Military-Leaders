# app/modules/hand_receipt/__init__.py

"""
Hand Receipt module package.

Exposes ORM models for:
- HandReceiptItem
- ItemCategory
- ItemCondition

Routers and services will be added in later backend phases.
"""

from .models import (
    HandReceiptItem,
    ItemCategory,
    ItemCondition,
)

__all__ = [
    "HandReceiptItem",
    "ItemCategory",
    "ItemCondition",
]


def get_router():
    """
    Minimal placeholder router so the module loads cleanly
    during backend Phase A (models only).
    """
    from fastapi import APIRouter

    router = APIRouter(
        prefix="/hand-receipt",
        tags=["hand_receipt"],
    )
    return router
