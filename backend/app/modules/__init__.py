# app/modules/__init__.py

"""
Module registry for dynamic router loading.
Every module listed in MODULES must contain:
    - api.py with a get_router() function
    - models.py imported so SQLAlchemy registers tables
"""

MODULES = [
    "auth",
    "soldier_profile",
    "military_info",   # <<< REQUIRED
]

# Ensure model modules are imported so SQLAlchemy sees them
from . import auth
from . import soldier_profile
from . import military_info

__all__ = [
    "MODULES",
]
