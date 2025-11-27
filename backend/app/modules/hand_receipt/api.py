"""API router scaffolding for `hand_receipt` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.HandReceiptRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for hand_receipt."""
        return []

    @router.post("/", response_model=schemas.HandReceiptRead)
    async def create_item(payload: schemas.HandReceiptCreate, db=Depends(get_db)):
        """Create placeholder item for hand_receipt."""
        return schemas.HandReceiptRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.HandReceiptRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.HandReceiptRead(id="example", data={"module": "hand_receipt"})

    return router
