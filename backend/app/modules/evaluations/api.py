"""API router scaffolding for `evaluations` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.EvaluationsRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for evaluations."""
        return []

    @router.post("/", response_model=schemas.EvaluationsRead)
    async def create_item(payload: schemas.EvaluationsCreate, db=Depends(get_db)):
        """Create placeholder item for evaluations."""
        return schemas.EvaluationsRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.EvaluationsRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.EvaluationsRead(id="example", data={"module": "evaluations"})

    return router
