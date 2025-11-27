"""API router scaffolding for `licenses` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.LicensesRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for licenses."""
        return []

    @router.post("/", response_model=schemas.LicensesRead)
    async def create_item(payload: schemas.LicensesCreate, db=Depends(get_db)):
        """Create placeholder item for licenses."""
        return schemas.LicensesRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.LicensesRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.LicensesRead(id="example", data={"module": "licenses"})

    return router
