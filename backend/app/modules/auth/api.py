# app/modules/auth/api.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.security import hash_password
from .schemas import UserCreate, UserRead
from .models import UserAccount

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"],
)


@router.post("/users", response_model=UserRead)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    # check unique email or username
    existing = db.query(UserAccount).filter(
        (UserAccount.username == data.username.lower()) |
        (UserAccount.email == data.email.lower())
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = UserAccount(
        username=data.username.lower(),
        email=data.email.lower(),
        password_hash=hash_password(data.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users", response_model=list[UserRead])
def list_users(db: Session = Depends(get_db)):
    return db.query(UserAccount).all()


def get_router():
    return router
