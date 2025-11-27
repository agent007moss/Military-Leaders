"""API router scaffolding for `appointments_tracker` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.AppointmentsTrackerRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for appointments_tracker."""
        return []

    @router.post("/", response_model=schemas.AppointmentsTrackerRead)
    async def create_item(payload: schemas.AppointmentsTrackerCreate, db=Depends(get_db)):
        """Create placeholder item for appointments_tracker."""
        return schemas.AppointmentsTrackerRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.AppointmentsTrackerRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.AppointmentsTrackerRead(id="example", data={"module": "appointments_tracker"})

    return router
