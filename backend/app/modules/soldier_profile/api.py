# app/modules/soldier_profile/api.py
"""
API router scaffolding for `soldier_profile` module.
Routes intentionally return placeholder static data.
"""

from fastapi import APIRouter, Depends
from app.core.db import get_db
from typing import Any, Dict


def get_router() -> APIRouter:
    router = APIRouter(
        prefix="/service-members",
        tags=["service_members"],
    )

    @router.get("/")
    async def list_service_members(db=Depends(get_db)) -> Dict[str, Any]:
        """
        Placeholder for list retrieval.
        No DB queries yet.
        """
        return {"status": "ok", "items": []}

    @router.post("/")
    async def create_service_member(db=Depends(get_db)) -> Dict[str, Any]:
        """
        Placeholder create.
        """
        return {
            "status": "created",
            "item": {
                "id": "placeholder-id",
                "message": "ServiceMember created (placeholder)",
            },
        }

    @router.get("/example")
    async def example_endpoint(db=Depends(get_db)) -> Dict[str, Any]:
        """
        Simple static response to verify router wiring.
        """
        return {
            "module": "soldier_profile",
            "example": True,
            "detail": "Router OK",
        }

    return router
