"""API router scaffolding for `battle_calendar` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.BattleCalendarRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for battle_calendar."""
        return []

    @router.post("/", response_model=schemas.BattleCalendarRead)
    async def create_item(payload: schemas.BattleCalendarCreate, db=Depends(get_db)):
        """Create placeholder item for battle_calendar."""
        return schemas.BattleCalendarRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.BattleCalendarRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.BattleCalendarRead(id="example", data={"module": "battle_calendar"})

    return router
