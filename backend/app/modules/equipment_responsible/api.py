"""API router scaffolding for `equipment_responsible` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.EquipmentResponsibleRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for equipment_responsible."""
        return []

    @router.post("/", response_model=schemas.EquipmentResponsibleRead)
    async def create_item(payload: schemas.EquipmentResponsibleCreate, db=Depends(get_db)):
        """Create placeholder item for equipment_responsible."""
        return schemas.EquipmentResponsibleRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.EquipmentResponsibleRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.EquipmentResponsibleRead(id="example", data={"module": "equipment_responsible"})

    return router
