"""API router scaffolding for `tasks` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.TasksRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for tasks."""
        return []

    @router.post("/", response_model=schemas.TasksRead)
    async def create_item(payload: schemas.TasksCreate, db=Depends(get_db)):
        """Create placeholder item for tasks."""
        return schemas.TasksRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.TasksRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.TasksRead(id="example", data={"module": "tasks"})

    return router
