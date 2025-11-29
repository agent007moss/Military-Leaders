# app/core/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./mlt.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_models():
    """
    Import ALL models that must exist in Phase 1 BEFORE creating tables.
    Only add new models as new modules go online.
    """
    from app.modules.auth.models import UserAccount
    from app.modules.soldier_profile.models import ServiceMember
    # Add additional Phase-1 models here as modules come online.

    # Create tables
    Base.metadata.create_all(bind=engine)
