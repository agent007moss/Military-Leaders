# app/core/settings.py

from __future__ import annotations

from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Environment
    environment: str = "development"

    # Database
    database_url: str = "sqlite:///./mlt.db"

    # JWT / Auth
    jwt_secret_key: str = "CHANGE_ME_SUPER_SECRET_KEY"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expires_minutes: int = 15
    jwt_refresh_token_expires_days: int = 7

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()
