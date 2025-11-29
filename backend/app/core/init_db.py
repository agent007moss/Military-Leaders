# app/core/init_db.py

"""
Database initialization helper for the Military Leaders backend.

Usage (from backend/):
    python -m app.core.init_db

This will import all models (via Base) and create tables in the configured DB.
"""

from __future__ import annotations

from sqlalchemy.exc import SQLAlchemyError

from app.core.db import engine, Base


def init_db() -> None:
    """
    Create all tables defined on the SQLAlchemy Base metadata.
    Safe to run multiple times; it will only create missing tables.
    """
    try:
        Base.metadata.create_all(bind=engine)
        print("[init_db] Database tables created or already present.")
    except SQLAlchemyError as exc:
        # Basic error logging; you can replace with structured logging later.
        print(f"[init_db] ERROR while creating tables: {exc}")
        raise


if __name__ == "__main__":
    init_db()
