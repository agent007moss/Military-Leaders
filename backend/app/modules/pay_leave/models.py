# app/modules/pay_leave/models.py

from __future__ import annotations

import enum
import uuid
from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    Enum as SAEnum,
    ForeignKey,
    Numeric,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from app.core.models_base import BaseModelMixin


# ============================================================
# ENUMS
# ============================================================

class LeaveType(str, enum.Enum):
    ORDINARY = "ORDINARY"
    EMERGENCY = "EMERGENCY"
    CONVALESCENT = "CONVALESCENT"
    MATERNITY_PATERNITY = "MATERNITY_PATERNITY"
    PTDY = "PTDY"
    ADOPTION = "ADOPTION"
    OTHER = "OTHER"


class PayStatusType(str, enum.Enum):
    PAID_GOOD_STANDING = "PAID_GOOD_STANDING"
    PENDING_PAY_ISSUE = "PENDING_PAY_ISSUE"
    BACK_PAY_PENDING = "BACK_PAY_PENDING"
    STOP_PAY = "STOP_PAY"
    DEBT_OVERPAYMENT = "DEBT_OVERPAYMENT"
    AUDIT_PENDING = "AUDIT_PENDING"
    OTHER = "OTHER"


# ============================================================
# MODEL: LeaveAccount
# ============================================================

class LeaveAccount(BaseModelMixin, Base):
    """
    Per-service-member leave balance + SLA rules.
    """

    __tablename__ = "leave_accounts"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("service_members.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    current_balance_days: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False,
        default=Decimal("0.00"),
    )

    use_or_lose_days: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False,
        default=Decimal("0.00"),
    )

    sla_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    sla_carryover_cap_days: Mapped[Optional[Decimal]] = mapped_column(
        Numeric(5, 2),
        nullable=True,
    )

    sla_expires_on: Mapped[Optional[date]] = mapped_column(
        Date,
        nullable=True,
    )

    last_accrual_run_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    last_balance_update_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    service_member: Mapped["ServiceMember"] = relationship("ServiceMember", backref="leave_account")


# ============================================================
# MODEL: LeaveEntry
# ============================================================

class LeaveEntry(BaseModelMixin, Base):
    """
    A single period of leave for a service member.
    """

    __tablename__ = "leave_entries"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("service_members.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=False)

    total_days: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False,
    )

    leave_type: Mapped[LeaveType] = mapped_column(
        SAEnum(LeaveType, name="leave_type_enum"),
        nullable=False,
    )

    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    was_subtracted_from_balance: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    service_member: Mapped["ServiceMember"] = relationship("ServiceMember", backref="leave_entries")


# ============================================================
# MODEL: PayStatusEntry
# ============================================================

class PayStatusEntry(BaseModelMixin, Base):
    """
    Pay status, issues, holds, audits.
    """

    __tablename__ = "pay_status_entries"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("service_members.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    status: Mapped[PayStatusType] = mapped_column(
        SAEnum(PayStatusType, name="pay_status_type_enum"),
        nullable=False,
    )

    status_start_date: Mapped[date] = mapped_column(Date, nullable=False)
    status_resolution_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)

    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    service_member: Mapped["ServiceMember"] = relationship("ServiceMember", backref="pay_status_entries")
