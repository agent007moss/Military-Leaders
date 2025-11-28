# app/modules/soldier_profile/__init__.py

from .models import (
    ServiceMember,
    ServiceMemberAdminData,
    ServiceMemberServiceData,
    ServiceMemberContactData,
    ServiceMemberStatusData,
)
from .api import get_router
from . import schemas

__all__ = [
    "ServiceMember",
    "ServiceMemberAdminData",
    "ServiceMemberServiceData",
    "ServiceMemberContactData",
    "ServiceMemberStatusData",
    "get_router",
    "schemas",
]

