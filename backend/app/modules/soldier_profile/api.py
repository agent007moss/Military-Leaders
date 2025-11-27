"""API router scaffolding for `soldier_profile` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.SoldierProfileRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for soldier_profile."""
        return []

    @router.post("/", response_model=schemas.SoldierProfileRead)
    async def create_item(payload: schemas.SoldierProfileCreate, db=Depends(get_db)):
        """Create placeholder item for soldier_profile."""
        return schemas.SoldierProfileRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.SoldierProfileRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.SoldierProfileRead(id="example", data={"module": "soldier_profile"})

    return router
