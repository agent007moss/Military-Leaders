from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import get_db
from .models import UserAccount
from .schemas import UserCreate, UserRead
from app.core.models_base import Role


def get_router() -> APIRouter:
    router = APIRouter(
        prefix="/auth",
        tags=["auth"],
    )

    @router.post("/users", response_model=UserRead)
    def create_user(payload: UserCreate, db: Session = Depends(get_db)):
        existing = (
            db.query(UserAccount)
            .filter(
                (UserAccount.username == payload.username)
                | (UserAccount.email == payload.email)
            )
            .first()
        )
        if existing:
            raise HTTPException(status_code=400, detail="Username or email already exists")

        user = UserAccount(
            username=payload.username,
            email=payload.email,
            password_hash=f"plain::{payload.password}",
            role=Role.StandardUser,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @router.get("/users", response_model=List[UserRead])
    def list_users(db: Session = Depends(get_db)):
        return db.query(UserAccount).all()

    return router
