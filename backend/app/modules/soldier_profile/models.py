# app/modules/soldier_profile/models.py

from __future__ import annotations

import uuid
from datetime import date
from typing import Optional

from sqlalchemy import (
    String,
    Date,
    ForeignKey,
    Enum as SAEnum,
    Boolean,
    Integer,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.core.db import Base
from app.core.models_base import (
    BaseModel,
    Branch,
    Component,
)


# ---------------------------------------------------------------------------
# SERVICE MEMBER (TOP-LEVEL PROFILE)
# ---------------------------------------------------------------------------

class ServiceMember(BaseModel):
    """
    Central profile table. One row per Soldier/Marine/Airman/Guardian/Sailor/Coastie.
    All Phase 1 modules attach via service_member_id.
    """

    __tablename__ = "service_members"

    # Identity
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    middle_initial: Mapped[Optional[str]] = mapped_column(String(1))

    branch: Mapped[Branch] = mapped_column(
        SAEnum(Branch, name="branch_enum", inherit_schema=True),
        nullable=False,
    )
    component: Mapped[Optional[Component]] = mapped_column(
        SAEnum(Component, name="component_enum", inherit_schema=True),
    )

    # A single “owner” user account creates/owns this soldier record.
    owner_user_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("user_accounts.id", ondelete="SET NULL"),
        nullable=True,
    )

    # Relationships – separate tables for logical grouping
    admin_data: Mapped[Optional["ServiceMemberAdminData"]] = relationship(
        "ServiceMemberAdminData",
        back_populates="service_member",
        uselist=False,
        cascade="all, delete-orphan",
    )

    service_data: Mapped[Optional["ServiceMemberServiceData"]] = relationship(
        "ServiceMemberServiceData",
        back_populates="service_member",
        uselist=False,
        cascade="all, delete-orphan",
    )

    contact_data: Mapped[Optional["ServiceMemberContactData"]] = relationship(
        "ServiceMemberContactData",
        back_populates="service_member",
        uselist=False,
        cascade="all, delete-orphan",
    )

    status_data: Mapped[Optional["ServiceMemberStatusData"]] = relationship(
        "ServiceMemberStatusData",
        back_populates="service_member",
        uselist=False,
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<ServiceMember id={self.id} {self.last_name}, {self.first_name} "
            f"branch={self.branch.value}>"
        )


# ---------------------------------------------------------------------------
# SECTION A: ADMINISTRATIVE DATA
# ---------------------------------------------------------------------------

class ServiceMemberAdminData(BaseModel):
    """
    Branch-specific administrative identifiers + personal administrative data.
    Mirrors ERB/SRB/ESR/vMPF/DirectAccess core fields.
    """

    __tablename__ = "service_member_admin_data"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )

    # DOD-level identifiers
    dodid: Mapped[Optional[str]] = mapped_column(String(64))
    ssn_last4: Mapped[Optional[str]] = mapped_column(String(4))
    dob: Mapped[Optional[date]] = mapped_column(Date)

    # Branch-specific MOS/AFSC/RATE fields
    mos: Mapped[Optional[str]] = mapped_column(String(32))
    afsc: Mapped[Optional[str]] = mapped_column(String(32))
    rate: Mapped[Optional[str]] = mapped_column(String(32))
    designator: Mapped[Optional[str]] = mapped_column(String(32))

    duty_title: Mapped[Optional[str]] = mapped_column(String(120))
    unit_name: Mapped[Optional[str]] = mapped_column(String(200))

    unit_code: Mapped[Optional[str]] = mapped_column(String(32), index=True)

    clearance_type: Mapped[Optional[str]] = mapped_column(String(64))
    clearance_date: Mapped[Optional[date]] = mapped_column(Date)

    service_member: Mapped[ServiceMember] = relationship(
        "ServiceMember", back_populates="admin_data"
    )


# ---------------------------------------------------------------------------
# SECTION B: SERVICE DATA (TIS/TIG/EAS/BASD/PEBD/ETS)
# ---------------------------------------------------------------------------

class ServiceMemberServiceData(BaseModel):
    """
    Tracks service-specific dates, TIS, TIG, separation dates, and status codes.
    """

    __tablename__ = "service_member_service_data"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )

    basd: Mapped[Optional[date]] = mapped_column(Date)
    pebd: Mapped[Optional[date]] = mapped_column(Date)
    diems: Mapped[Optional[date]] = mapped_column(Date)
    dor: Mapped[Optional[date]] = mapped_column(Date)

    ets_eas: Mapped[Optional[date]] = mapped_column(Date)
    dos_eaos: Mapped[Optional[date]] = mapped_column(Date)

    # Derived values (computed in future phases)
    tis_years: Mapped[Optional[int]] = mapped_column(Integer)
    tig_years: Mapped[Optional[int]] = mapped_column(Integer)

    service_member: Mapped[ServiceMember] = relationship(
        "ServiceMember", back_populates="service_data"
    )


# ---------------------------------------------------------------------------
# SECTION C: CONTACT DATA
# ---------------------------------------------------------------------------

class ServiceMemberContactData(BaseModel):
    """
    Mailing, phone, email, personal contact info.
    """

    __tablename__ = "service_member_contact_data"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )

    phone: Mapped[Optional[str]] = mapped_column(String(32))
    email_mil: Mapped[Optional[str]] = mapped_column(String(250))
    email_civ: Mapped[Optional[str]] = mapped_column(String(250))

    address: Mapped[Optional[str]] = mapped_column(String(300))
    marital_status: Mapped[Optional[str]] = mapped_column(String(32))

    service_member: Mapped[ServiceMember] = relationship(
        "ServiceMember", back_populates="contact_data"
    )


# ---------------------------------------------------------------------------
# SECTION D: STATUS DATA (LEAVE / QUARTERS / MISSION / PDY)
# ---------------------------------------------------------------------------

class ServiceMemberStatusData(BaseModel):
    """
    Current duty status required by PERSTATS and Dashboard specification.
    """

    __tablename__ = "service_member_status_data"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )

    status: Mapped[Optional[str]] = mapped_column(String(50))
    status_detail: Mapped[Optional[str]] = mapped_column(String(200))

    on_leave: Mapped[bool] = mapped_column(Boolean, default=False)
    on_quarters: Mapped[bool] = mapped_column(Boolean, default=False)
    on_recovery: Mapped[bool] = mapped_column(Boolean, default=False)
    on_mission: Mapped[bool] = mapped_column(Boolean, default=False)

    last_status_update: Mapped[Optional[date]] = mapped_column(Date)

    service_member: Mapped[ServiceMember] = relationship(
        "ServiceMember", back_populates="status_data"
    )

