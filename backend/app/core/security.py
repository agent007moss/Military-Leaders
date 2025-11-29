# app/core/security.py

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional

from jose import jwt, JWTError
from passlib.context import CryptContext

from app.core.settings import get_settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, password_hash: str) -> bool:
    return pwd_context.verify(plain_password, password_hash)


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
