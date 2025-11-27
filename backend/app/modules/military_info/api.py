"""API router scaffolding for `military_info` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.MilitaryInfoRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for military_info."""
        return []

    @router.post("/", response_model=schemas.MilitaryInfoRead)
    async def create_item(payload: schemas.MilitaryInfoCreate, db=Depends(get_db)):
        """Create placeholder item for military_info."""
        return schemas.MilitaryInfoRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.MilitaryInfoRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.MilitaryInfoRead(id="example", data={"module": "military_info"})

    return router
