"""API router scaffolding for `dashboard` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.DashboardRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for dashboard."""
        return []

    @router.post("/", response_model=schemas.DashboardRead)
    async def create_item(payload: schemas.DashboardCreate, db=Depends(get_db)):
        """Create placeholder item for dashboard."""
        return schemas.DashboardRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.DashboardRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.DashboardRead(id="example", data={"module": "dashboard"})

    return router
