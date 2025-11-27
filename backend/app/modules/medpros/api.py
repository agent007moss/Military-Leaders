"""API router scaffolding for `medpros` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.MedprosRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for medpros."""
        return []

    @router.post("/", response_model=schemas.MedprosRead)
    async def create_item(payload: schemas.MedprosCreate, db=Depends(get_db)):
        """Create placeholder item for medpros."""
        return schemas.MedprosRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.MedprosRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.MedprosRead(id="example", data={"module": "medpros"})

    return router
