"""API router scaffolding for `counseling` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.CounselingRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for counseling."""
        return []

    @router.post("/", response_model=schemas.CounselingRead)
    async def create_item(payload: schemas.CounselingCreate, db=Depends(get_db)):
        """Create placeholder item for counseling."""
        return schemas.CounselingRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.CounselingRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.CounselingRead(id="example", data={"module": "counseling"})

    return router
