"""API router scaffolding for `flags_ucmj` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.FlagsUcmjRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for flags_ucmj."""
        return []

    @router.post("/", response_model=schemas.FlagsUcmjRead)
    async def create_item(payload: schemas.FlagsUcmjCreate, db=Depends(get_db)):
        """Create placeholder item for flags_ucmj."""
        return schemas.FlagsUcmjRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.FlagsUcmjRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.FlagsUcmjRead(id="example", data={"module": "flags_ucmj"})

    return router
