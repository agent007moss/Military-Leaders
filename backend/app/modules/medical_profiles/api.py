"""API router scaffolding for `medical_profiles` module.

Routes are intentionally non-functional and only return static placeholders.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.core.db import get_db  # placeholder
from . import schemas


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=List[schemas.MedicalProfilesRead])
    async def list_items(db=Depends(get_db)):
        """List placeholder items for medical_profiles."""
        return []

    @router.post("/", response_model=schemas.MedicalProfilesRead)
    async def create_item(payload: schemas.MedicalProfilesCreate, db=Depends(get_db)):
        """Create placeholder item for medical_profiles."""
        return schemas.MedicalProfilesRead(id="placeholder", data=payload.data)

    @router.get("/example", response_model=schemas.MedicalProfilesRead)
    async def example(db=Depends(get_db)):
        """Simple example endpoint to verify wiring."""
        return schemas.MedicalProfilesRead(id="example", data={"module": "medical_profiles"})

    return router
