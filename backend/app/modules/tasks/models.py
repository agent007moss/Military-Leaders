# app/modules/tasks/models.py

from __future__ import annotations

import enum
import uuid
from datetime import date
from typing import Optional

from sqlalchemy import (
    Date,
    Enum as SAEnum,
    Text,
    String,
    Boolean,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base
from app.core.models_base import BaseModelMixin


# -------------------------------------------------------
# ENUMS
# -------------------------------------------------------

class TaskType(str, enum.Enum):
    """
    Universal baseline list; admins extend via metadata.
    """
    APPOINTMENT = "APPOINTMENT"
    DOCUMENT_UPDATE = "DOCUMENT_UPDATE"
    HR_ACTION = "HR_ACTION"
    ADMIN_ACTION = "ADMIN_ACTION"
    MEDICAL = "MEDICAL"
    FITNESS = "FITNESS"
    TRAINING = "TRAINING"
    WEAPON_RANGE = "WEAPON_RANGE"
    COUNSELING = "COUNSELING"
    COMMAND_DIRECTED = "COMMAND_DIRECTED"
    SAFETY = "SAFETY"
    EQUIPMENT_TURN_IN = "EQUIPMENT_TURN_IN"
    OTHER = "OTHER"


class TaskStatusColor(str, enum.Enum):
    """
    Stored color so frontends do not re-evaluate logic.
    """
    GREEN = "GREEN"
    AMBER = "AMBER"
    RED = "RED"
    GRAY = "GRAY"  # completed


# -------------------------------------------------------
# MODEL: TaskEntry
# -------------------------------------------------------

class TaskEntry(BaseModelMixin, Base):
    """
    Represents a single task assigned to a soldier.

    Domain logic (color rules, notifications, SLA) is handled
    by service layers in future phases.
    """

    __tablename__ = "task_entries"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    # Basic information
    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    task_type: Mapped[TaskType] = mapped_column(
        SAEnum(TaskType, name="task_type_enum"),
        nullable=False,
    )

    description: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    # Assigned-by identity
    assigned_by_rank: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    assigned_by_last: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    assigned_by_first: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    assigned_by_phone: Mapped[Optional[str]] = mapped_column(
        String(25),
        nullable=True,
    )

    # Required dates
    date_assigned: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    suspense_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    # Pre-computed color for UI
    status_color: Mapped[TaskStatusColor] = mapped_column(
        SAEnum(TaskStatusColor, name="task_status_color_enum"),
        nullable=False,
    )

    # Completion tracking
    is_completed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    completion_date: Mapped[Optional[date]] = mapped_column(
        Date,
        nullable=True,
    )

    # Attachments placeholder (Phase 2 integration)
    attachment_refs: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    def __repr__(self) -> str:  # debug helper
        return (
            f"<TaskEntry id={self.id} soldier={self.soldier_id} "
            f"title={self.title!r} status={self.status_color}>"
        )
