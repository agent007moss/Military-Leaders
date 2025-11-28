from __future__ import annotations

from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import Field
import os


class Settings(BaseSettings):
    """
    Global application configuration.
    """

    # ------------------------------------------------------------------
    # APP METADATA
    # ------------------------------------------------------------------
    app_name: str = "Military Leaders Tool - Phase 1 Skeleton"
    debug: bool = True

    # ------------------------------------------------------------------
    # DATABASE CONFIG
    # ------------------------------------------------------------------
    # Default SQLite DB inside backend directory
    database_url: str = Field(
        default="sqlite:///./mlt.db",
        description="Default SQLite DB for Phase 1"
    )

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    """
    Cached settings loader.
    """
    settings = Settings()

    # Ensure SQLite directory exists if using sqlite:///./xyz.db
    if settings.database_url.startswith("sqlite:///"):
        db_path = settings.database_url.replace("sqlite:///", "")
        db_dir = os.path.dirname(db_path)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir, exist_ok=True)

    return settings
