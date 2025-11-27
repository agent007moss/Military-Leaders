"""API router scaffolding for `physical_fitness` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.PhysicalFitnessRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for physical_fitness."""
        return []

    @router.post("/", response_model=schemas.PhysicalFitnessRead)
    async def create_item(payload: schemas.PhysicalFitnessCreate, db=Depends(get_db)):
        """Create placeholder item for physical_fitness."""
        return schemas.PhysicalFitnessRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.PhysicalFitnessRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.PhysicalFitnessRead(id="example", data={"module": "physical_fitness"})

    return router
