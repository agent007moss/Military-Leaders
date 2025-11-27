"""API router scaffolding for `weapons` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.WeaponsRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for weapons."""
        return []

    @router.post("/", response_model=schemas.WeaponsRead)
    async def create_item(payload: schemas.WeaponsCreate, db=Depends(get_db)):
        """Create placeholder item for weapons."""
        return schemas.WeaponsRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.WeaponsRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.WeaponsRead(id="example", data={"module": "weapons"})

    return router
