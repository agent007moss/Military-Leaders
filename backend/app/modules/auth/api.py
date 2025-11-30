from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
)
from .models import UserAccount
from .schemas import (
    UserCreate,
    UserRead,
    LoginRequest,
    RefreshRequest,
    TokenPair,
)
from .dependencies import get_current_user

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"],
)


# -------------------------------------------------
# Create user (registration core function)
# -------------------------------------------------
@router.post("/users", response_model=UserRead)
def create_user(data: UserCreate, db: Session = Depends(get_db)) -> UserRead:
    username = data.username.lower()
    email = data.email.lower()

    existing = (
        db.query(UserAccount)
        .filter(
            (UserAccount.username == username)
            | (UserAccount.email == email)
        )
        .first()
    )
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = UserAccount(
        username=username,
        email=email,
        password_hash=hash_password(data.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# -------------------------------------------------
# Register (clean endpoint)  <-- NEW
# -------------------------------------------------
@router.post("/register", response_model=UserRead)
def register_user(data: UserCreate, db: Session = Depends(get_db)) -> UserRead:
    return create_user(data, db)


# -------------------------------------------------
# List users (temporary, open)
# -------------------------------------------------
@router.get("/users", response_model=List[UserRead])
def list_users(db: Session = Depends(get_db)) -> List[UserRead]:
    return db.query(UserAccount).all()


# -------------------------------------------------
# Login -> access + refresh tokens
# -------------------------------------------------
@router.post("/login", response_model=TokenPair)
def login(data: LoginRequest, db: Session = Depends(get_db)) -> TokenPair:
    identifier = data.username_or_email.lower()

    user = (
        db.query(UserAccount)
        .filter(
            (UserAccount.username == identifier)
            | (UserAccount.email == identifier)
        )
        .first()
    )

    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    access_token = create_access_token(str(user.id))
    refresh_token = create_refresh_token(str(user.id))

    return TokenPair(
        access_token=access_token,
        refresh_token=refresh_token,
    )


# -------------------------------------------------
# Refresh tokens
# -------------------------------------------------
from jose import JWTError
from app.core.security import decode_token


@router.post("/refresh", response_model=TokenPair)
def refresh_tokens(data: RefreshRequest, db: Session = Depends(get_db)) -> TokenPair:
    try:
        payload = decode_token(data.refresh_token)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )

    if payload.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token type",
        )

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
        )

    user = db.query(UserAccount).filter(UserAccount.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    access_token = create_access_token(str(user.id))
    refresh_token = create_refresh_token(str(user.id))

    return TokenPair(
        access_token=access_token,
        refresh_token=refresh_token,
    )


# -------------------------------------------------
# Get current user (/me)
# -------------------------------------------------
@router.get("/me", response_model=UserRead)
def read_current_user(current_user: UserAccount = Depends(get_current_user)) -> UserRead:
    return current_user


def get_router():
    return router
