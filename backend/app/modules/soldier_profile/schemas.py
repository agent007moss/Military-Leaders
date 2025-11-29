# app/modules/soldier_profile/schemas.py

"""
Pydantic v2 schemas for the ServiceMember profile module.

These are DTOs only – no business logic.
They are designed to map 1:1 to the SQLAlchemy models in models.py.
"""

from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

from app.core.models_base import Branch, Component


# ---------------------------------------------------------------------------
# BASE SECTION SCHEMAS (Admin / Service / Contact / Status)
# ---------------------------------------------------------------------------


class ServiceMemberAdminDataBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    dodid: Optional[str] = Field(default=None, max_length=64)
    ssn_last4: Optional[str] = Field(default=None, max_length=4)
    dob: Optional[date] = None

    mos: Optional[str] = Field(default=None, max_length=32)
    afsc: Optional[str] = Field(default=None, max_length=32)
    rate: Optional[str] = Field(default=None, max_length=32)
    designator: Optional[str] = Field(default=None, max_length=32)

    duty_title: Optional[str] = Field(default=None, max_length=120)
    unit_name: Optional[str] = Field(default=None, max_length=200)

    unit_code: Optional[str] = Field(default=None, max_length=32)

    clearance_type: Optional[str] = Field(default=None, max_length=64)
    clearance_date: Optional[date] = None


class ServiceMemberAdminDataCreate(ServiceMemberAdminDataBase):
    """Create payload for admin data (all optional for now)."""

    pass


class ServiceMemberAdminDataUpdate(ServiceMemberAdminDataBase):
    """Update payload – all fields optional, used as partial update."""

    pass


class ServiceMemberAdminDataRead(ServiceMemberAdminDataBase):
    """Read DTO for admin data; includes owning service_member_id."""

    service_member_id: str


# ---------------------------------------------------------------------------


class ServiceMemberServiceDataBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    basd: Optional[date] = None
    pebd: Optional[date] = None
    diems: Optional[date] = None
    dor: Optional[date] = None

    ets_eas: Optional[date] = None
    dos_eaos: Optional[date] = None

    tis_years: Optional[int] = Field(default=None, ge=0)
    tig_years: Optional[int] = Field(default=None, ge=0)


class ServiceMemberServiceDataCreate(ServiceMemberServiceDataBase):
    pass


class ServiceMemberServiceDataUpdate(ServiceMemberServiceDataBase):
    pass


class ServiceMemberServiceDataRead(ServiceMemberServiceDataBase):
    service_member_id: str


# ---------------------------------------------------------------------------


class ServiceMemberContactDataBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    phone: Optional[str] = Field(default=None, max_length=32)
    email_mil: Optional[str] = Field(default=None, max_length=250)
    email_civ: Optional[str] = Field(default=None, max_length=250)

    address: Optional[str] = Field(default=None, max_length=300)
    marital_status: Optional[str] = Field(default=None, max_length=32)


class ServiceMemberContactDataCreate(ServiceMemberContactDataBase):
    pass


class ServiceMemberContactDataUpdate(ServiceMemberContactDataBase):
    pass


class ServiceMemberContactDataRead(ServiceMemberContactDataBase):
    service_member_id: str


# ---------------------------------------------------------------------------


class ServiceMemberStatusDataBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: Optional[str] = Field(default=None, max_length=50)
    status_detail: Optional[str] = Field(default=None, max_length=200)

    on_leave: bool = False
    on_quarters: bool = False
    on_recovery: bool = False
    on_mission: bool = False

    last_status_update: Optional[date] = None


class ServiceMemberStatusDataCreate(ServiceMemberStatusDataBase):
    pass


class ServiceMemberStatusDataUpdate(ServiceMemberStatusDataBase):
    pass


class ServiceMemberStatusDataRead(ServiceMemberStatusDataBase):
    service_member_id: str


# ---------------------------------------------------------------------------
# TOP-LEVEL SERVICEMEMBER SCHEMAS
# ---------------------------------------------------------------------------


class ServiceMemberBase(BaseModel):
    """
    Common fields for ServiceMember create/update.
    """

    model_config = ConfigDict(from_attributes=True)

    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)
    middle_initial: Optional[str] = Field(default=None, max_length=1)

    branch: Branch
    component: Optional[Component] = None


class ServiceMemberCreate(ServiceMemberBase):
    """
    Create payload for a ServiceMember.
    Nested section payloads are optional for Phase 1 and can be
    created together with the core ServiceMember.
    """

    owner_user_id: Optional[str] = None  # UUID as string for now

    admin_data: Optional[ServiceMemberAdminDataCreate] = None
    service_data: Optional[ServiceMemberServiceDataCreate] = None
    contact_data: Optional[ServiceMemberContactDataCreate] = None
    status_data: Optional[ServiceMemberStatusDataCreate] = None


class ServiceMemberUpdate(BaseModel):
    """
    Partial update payload – all fields optional.
    """

    model_config = ConfigDict(from_attributes=True)

    first_name: Optional[str] = Field(default=None, max_length=100)
    last_name: Optional[str] = Field(default=None, max_length=100)
    middle_initial: Optional[str] = Field(default=None, max_length=1)

    branch: Optional[Branch] = None
    component: Optional[Component] = None

    owner_user_id: Optional[str] = None

    admin_data: Optional[ServiceMemberAdminDataUpdate] = None
    service_data: Optional[ServiceMemberServiceDataUpdate] = None
    contact_data: Optional[ServiceMemberContactDataUpdate] = None
    status_data: Optional[ServiceMemberStatusDataUpdate] = None


class ServiceMemberRead(ServiceMemberBase):
    """
    Full read model for a ServiceMember, including nested sections.
    """

    id: str
    created_at: date | None = None
    updated_at: date | None = None

    owner_user_id: Optional[str] = None

    admin_data: Optional[ServiceMemberAdminDataRead] = None
    service_data: Optional[ServiceMemberServiceDataRead] = None
    contact_data: Optional[ServiceMemberContactDataRead] = None
    status_data: Optional[ServiceMemberStatusDataRead] = None
