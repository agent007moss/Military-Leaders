from __future__ import annotations

from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import get_db
from .models import ServiceMember
from .schemas import ServiceMemberCreate, ServiceMemberRead


def get_router() -> APIRouter:
    router = APIRouter(
    	prefix="/api/soldier-profile",
    	tags=["service_members"],
    )


    @router.get("/", response_model=List[ServiceMemberRead])
    def list_service_members(db: Session = Depends(get_db)):
        return db.query(ServiceMember).all()

    @router.get("/{service_member_id}", response_model=ServiceMemberRead)
    def get_service_member(service_member_id: UUID, db: Session = Depends(get_db)):
        obj = db.query(ServiceMember).filter(ServiceMember.id == service_member_id).first()
        if not obj:
            raise HTTPException(status_code=404, detail="Service member not found")
        return obj

    @router.post("/", response_model=ServiceMemberRead)
    def create_service_member(payload: ServiceMemberCreate, db: Session = Depends(get_db)):
        obj = ServiceMember(
            first_name=payload.first_name,
            last_name=payload.last_name,
            middle_initial=payload.middle_initial,
            branch=payload.branch,
            component=payload.component,
            owner_user_id=payload.owner_user_id,
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    return router
