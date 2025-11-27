"""API router scaffolding for `appointments` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.AppointmentsRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for appointments."""
        return []

    @router.post("/", response_model=schemas.AppointmentsRead)
    async def create_item(payload: schemas.AppointmentsCreate, db=Depends(get_db)):
        """Create placeholder item for appointments."""
        return schemas.AppointmentsRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.AppointmentsRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.AppointmentsRead(id="example", data={"module": "appointments"})

    return router
