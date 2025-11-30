# app/modules/military_info/__init__.py

"""
Military Info (Master Personnel Record) module.

Ensures models are loaded for SQLAlchemy table registration,
and exposes the API router factory.
"""

# Ensure models import so SQLAlchemy registers all tables
from . import models

# Expose get_router()
from .api import get_router

__all__ = [
    "get_router",
]
