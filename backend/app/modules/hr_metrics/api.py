"""API router scaffolding for `hr_metrics` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.HrMetricsRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for hr_metrics."""
        return []

    @router.post("/", response_model=schemas.HrMetricsRead)
    async def create_item(payload: schemas.HrMetricsCreate, db=Depends(get_db)):
        """Create placeholder item for hr_metrics."""
        return schemas.HrMetricsRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.HrMetricsRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.HrMetricsRead(id="example", data={"module": "hr_metrics"})

    return router
