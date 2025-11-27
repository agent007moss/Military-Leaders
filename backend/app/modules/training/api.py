"""API router scaffolding for `training` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.TrainingRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for training."""
        return []

    @router.post("/", response_model=schemas.TrainingRead)
    async def create_item(payload: schemas.TrainingCreate, db=Depends(get_db)):
        """Create placeholder item for training."""
        return schemas.TrainingRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.TrainingRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.TrainingRead(id="example", data={"module": "training"})

    return router
