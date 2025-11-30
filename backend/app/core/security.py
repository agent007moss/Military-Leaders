from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional

from jose import jwt, JWTError
from passlib.context import CryptContext

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.settings import get_settings
from app.core.db import get_db
from app.modules.auth.models import UserAccount

# -------------------------------------------------------------------------
# PASSWORD HASHING
# -------------------------------------------------------------------------

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, password_hash: str) -> bool:
    return pwd_context.verify(plain_password, password_hash)


# -------------------------------------------------------------------------
# JWT HELPERS
# -------------------------------------------------------------------------

def _jwt_base_payload(subject: str, token_type: str) -> Dict[str, Any]:
    now = datetime.now(timezone.utc)
    return {
        "sub": subject,
        "type": token_type,
        "iat": int(now.timestamp()),
    }


def create_access_token(subject: str, extra_claims: Optional[Dict[str, Any]] = None) -> str:
    settings = get_settings()
    payload = _jwt_base_payload(subject, "access")

    if extra_claims:
        payload.update(extra_claims)

    exp = datetime.now(timezone.utc) + timedelta(
        minutes=settings.jwt_access_token_expires_minutes
    )
    payload["exp"] = int(exp.timestamp())

    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def create_refresh_token(subject: str, extra_claims: Optional[Dict[str, Any]] = None) -> str:
    settings = get_settings()
    payload = _jwt_base_payload(subject, "refresh")

    if extra_claims:
        payload.update(extra_claims)

    exp = datetime.now(timezone.utc) + timedelta(
        days=settings.jwt_refresh_token_expires_days
    )
    payload["exp"] = int(exp.timestamp())

    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def decode_token(token: str) -> Dict[str, Any]:
    """
    Decode a JWT and return its payload.
    Raises jose.JWTError on invalid/expired token.
    """
    settings = get_settings()
    return jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])


# -------------------------------------------------------------------------
# AUTH DEPENDENCY: get_current_user
# -------------------------------------------------------------------------

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> UserAccount:
    """Extract user from JWT access token."""
    unauthorized = HTTPException(status_code=401, detail="Invalid or expired token")

    try:
        payload = decode_token(token)
    except JWTError:
        raise unauthorized

    if payload.get("type") != "access":
        raise unauthorized

    user_id = payload.get("sub")
    if not user_id:
        raise unauthorized

    user = db.query(UserAccount).filter(UserAccount.id == user_id).first()
    if not user:
        raise unauthorized

    return user
