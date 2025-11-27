"""API router scaffolding for `rating_scheme` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.RatingSchemeRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for rating_scheme."""
        return []

    @router.post("/", response_model=schemas.RatingSchemeRead)
    async def create_item(payload: schemas.RatingSchemeCreate, db=Depends(get_db)):
        """Create placeholder item for rating_scheme."""
        return schemas.RatingSchemeRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.RatingSchemeRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.RatingSchemeRead(id="example", data={"module": "rating_scheme"})

    return router
