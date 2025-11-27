"""API router scaffolding for `pay_leave` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.PayLeaveRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for pay_leave."""
        return []

    @router.post("/", response_model=schemas.PayLeaveRead)
    async def create_item(payload: schemas.PayLeaveCreate, db=Depends(get_db)):
        """Create placeholder item for pay_leave."""
        return schemas.PayLeaveRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.PayLeaveRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.PayLeaveRead(id="example", data={"module": "pay_leave"})

    return router
