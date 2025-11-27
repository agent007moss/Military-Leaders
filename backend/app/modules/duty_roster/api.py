"""API router scaffolding for `duty_roster` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.DutyRosterRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for duty_roster."""
        return []

    @router.post("/", response_model=schemas.DutyRosterRead)
    async def create_item(payload: schemas.DutyRosterCreate, db=Depends(get_db)):
        """Create placeholder item for duty_roster."""
        return schemas.DutyRosterRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.DutyRosterRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.DutyRosterRead(id="example", data={"module": "duty_roster"})

    return router
