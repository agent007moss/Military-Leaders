"""API router scaffolding for `awards` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.AwardsRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for awards."""
        return []

    @router.post("/", response_model=schemas.AwardsRead)
    async def create_item(payload: schemas.AwardsCreate, db=Depends(get_db)):
        """Create placeholder item for awards."""
        return schemas.AwardsRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.AwardsRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.AwardsRead(id="example", data={"module": "awards"})

    return router
