"""API router scaffolding for `auth` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.AuthRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for auth."""
        return []

    @router.post("/", response_model=schemas.AuthRead)
    async def create_item(payload: schemas.AuthCreate, db=Depends(get_db)):
        """Create placeholder item for auth."""
        return schemas.AuthRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.AuthRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.AuthRead(id="example", data={"module": "auth"})

    return router
