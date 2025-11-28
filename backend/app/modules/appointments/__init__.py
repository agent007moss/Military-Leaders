# app/modules/appointments/__init__.py

from .models import Appointment
from .api import get_router
from . import schemas

__all__ = [
    "Appointment",
    "get_router",
    "schemas",
]

