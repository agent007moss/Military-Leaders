# app/modules/military_info/api_admin_data.py

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.core.db import get_db
from app.core.security import get_current_user

from .models import AdminData
from .schemas import AdminDataRead


router = APIRouter(
    prefix="/api/military-info/admin-data",
    tags=["military_info_admin_data"],
)


@router.post("/", response_model=AdminDataRead)
def create_admin_data(
    payload: dict,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """Create or replace a service member’s AdminData block."""

    soldier_id = payload.get("soldier_id")
    if not soldier_id:
        raise HTTPException(status_code=400, detail="soldier_id is required")

    # Delete old entry if exists (1:1 table)
    db.query(AdminData).filter(AdminData.soldier_id == soldier_id).delete()

    obj = AdminData(**payload)
    db.add(obj)
    db.commit()
    db.refresh(obj)

    return obj
