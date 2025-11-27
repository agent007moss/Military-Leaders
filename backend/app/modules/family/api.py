"""API router scaffolding for `family` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.FamilyRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for family."""
        return []

    @router.post("/", response_model=schemas.FamilyRead)
    async def create_item(payload: schemas.FamilyCreate, db=Depends(get_db)):
        """Create placeholder item for family."""
        return schemas.FamilyRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.FamilyRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.FamilyRead(id="example", data={"module": "family"})

    return router
