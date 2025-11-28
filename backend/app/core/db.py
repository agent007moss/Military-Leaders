from __future__ import annotations

from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from .settings import get_settings


# ------------------------------------------------------------------
# LOAD SETTINGS
# ------------------------------------------------------------------
settings = get_settings()
DATABASE_URL = settings.database_url


# ------------------------------------------------------------------
# DATABASE ENGINE (SQLite for Phase 1)
# ------------------------------------------------------------------
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
    if DATABASE_URL.startswith("sqlite")
    else {},
    echo=False,
    future=True,
)


# ------------------------------------------------------------------
# SESSION LOCAL
# ------------------------------------------------------------------
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False,
    class_=Session,
)


# ------------------------------------------------------------------
# BASE CLASS FOR MODELS
# ------------------------------------------------------------------
Base = declarative_base()


# ------------------------------------------------------------------
# FASTAPI DEPENDENCY: DB SESSION
# ------------------------------------------------------------------
def get_db() -> Generator[Session, None, None]:
    """
    Provides a SQLAlchemy Session to request handlers.
    Always closes after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
