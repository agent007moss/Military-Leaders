# app/modules/military_info/__init__.py

"""
Military Info (Master Personnel Record) module.

Provides a unified read-only API endpoint to fetch the complete
"Military Info Box" / ERB-STP style bundle for a single service member.
"""

from .api import get_router  # main FastAPI router factory
from . import models  # ensure models are imported so tables are registered

__all__ = [
    "get_router",
]
