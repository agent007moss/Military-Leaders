from __future__ import annotations

import uuid
from datetime import date
from typing import Optional

from sqlalchemy import (
    String,
    Date,
    Text,
    Enum as SAEnum,
    ForeignKey,
    Integer,
)
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PGUUID

from app.core.db import Base
from app.core.models_base import BaseModelMixin, Branch, Component


# ---------------------------------------------------------------------------
# MASTER PERSONNEL RECORD — ADMINISTRATIVE DATA
# ---------------------------------------------------------------------------

class AdminData(BaseModelMixin, Base):
    """
    Section A: Administrative Data (branch-specific fields allowed).
    """
    __tablename__ = "admin_data"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    # Universal
    last_name: Mapped[Optional[str]] = mapped_column(String(50))
    first_name: Mapped[Optional[str]] = mapped_column(String(50))
    middle_initial: Mapped[Optional[str]] = mapped_column(String(5))
    rank: Mapped[Optional[str]] = mapped_column(String(20))
    grade: Mapped[Optional[str]] = mapped_column(String(5))
    dodid: Mapped[Optional[str]] = mapped_column(String(20))
    ssn_last4: Mapped[Optional[str]] = mapped_column(String(4))
    dob: Mapped[Optional[date]] = mapped_column(Date)
    gender: Mapped[Optional[str]] = mapped_column(String(20))
    component: Mapped[Optional[Component]] = mapped_column(
        SAEnum(Component, name="component_enum")
    )
    branch: Mapped[Optional[Branch]] = mapped_column(
        SAEnum(Branch, name="branch_enum")
    )
    unit: Mapped[Optional[str]] = mapped_column(String(100))
    uic_ruc_pas_opfac: Mapped[Optional[str]] = mapped_column(String(20))
    duty_title: Mapped[Optional[str]] = mapped_column(String(200))
    duty_location: Mapped[Optional[str]] = mapped_column(String(200))
    security_clearance: Mapped[Optional[str]] = mapped_column(String(50))
    clearance_date: Mapped[Optional[date]] = mapped_column(Date)
    marital_status: Mapped[Optional[str]] = mapped_column(String(50))
    address: Mapped[Optional[str]] = mapped_column(Text)
    phone: Mapped[Optional[str]] = mapped_column(String(20))
    email_mil: Mapped[Optional[str]] = mapped_column(String(100))
    email_civ: Mapped[Optional[str]] = mapped_column(String(100))
    pmos_afsc_rate: Mapped[Optional[str]] = mapped_column(String(50))


# ---------------------------------------------------------------------------
# SERVICE DATA (TIS/TIG/PAY/STATUS)
# ---------------------------------------------------------------------------

class ServiceData(BaseModelMixin, Base):
    """
    Section B: Service Data.
    """
    __tablename__ = "service_data"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    basd: Mapped[Optional[date]] = mapped_column(Date)
    pebd: Mapped[Optional[date]] = mapped_column(Date)
    diems: Mapped[Optional[date]] = mapped_column(Date)
    ets_eas_eaos_dos: Mapped[Optional[date]] = mapped_column(Date)
    tis_years: Mapped[Optional[int]] = mapped_column(Integer)
    tig_years: Mapped[Optional[int]] = mapped_column(Integer)
    pay_grade: Mapped[Optional[str]] = mapped_column(String(5))
    promotion_eligibility: Mapped[Optional[str]] = mapped_column(String(200))
    flag_status: Mapped[Optional[str]] = mapped_column(String(200))
    component_status: Mapped[Optional[str]] = mapped_column(String(100))


# ---------------------------------------------------------------------------
# MILITARY EDUCATION
# ---------------------------------------------------------------------------

class MilitaryEducation(BaseModelMixin, Base):
    """
    Section C1: Military Schools.
    """
    __tablename__ = "military_education"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    course_name: Mapped[str] = mapped_column(String(200))
    start_date: Mapped[Optional[date]] = mapped_column(Date)
    end_date: Mapped[Optional[date]] = mapped_column(Date)
    resident: Mapped[Optional[bool]] = mapped_column()
    certificate_ref: Mapped[Optional[str]] = mapped_column(Text)
    notes: Mapped[Optional[str]] = mapped_column(Text)


class CivilianEducation(BaseModelMixin, Base):
    """
    Section C2: Civilian Education.
    """
    __tablename__ = "civilian_education"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    highest_degree: Mapped[Optional[str]] = mapped_column(String(100))
    major: Mapped[Optional[str]] = mapped_column(String(100))
    school_name: Mapped[Optional[str]] = mapped_column(String(200))
    completion_date: Mapped[Optional[date]] = mapped_column(Date)
    credits: Mapped[Optional[int]] = mapped_column(Integer)


# ---------------------------------------------------------------------------
# AWARDS SUMMARY
# ---------------------------------------------------------------------------

class AwardSummary(BaseModelMixin, Base):
    """
    Section D: Awards & Decorations (summary mirror of Awards Box).
    """
    __tablename__ = "award_summary"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    award_type: Mapped[str] = mapped_column(String(50))
    count: Mapped[Optional[int]] = mapped_column(Integer)
    last_award_date: Mapped[Optional[date]] = mapped_column(Date)
    award_periods_ref: Mapped[Optional[str]] = mapped_column(Text)


# ---------------------------------------------------------------------------
# ASSIGNMENT HISTORY
# ---------------------------------------------------------------------------

class AssignmentHistory(BaseModelMixin, Base):
    """
    Section E: Assignment History.
    """
    __tablename__ = "assignment_history"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    unit: Mapped[Optional[str]] = mapped_column(String(200))
    station: Mapped[Optional[str]] = mapped_column(String(200))
    uic_ruc_pas_opfac: Mapped[Optional[str]] = mapped_column(String(20))
    from_date: Mapped[Optional[date]] = mapped_column(Date)
    to_date: Mapped[Optional[date]] = mapped_column(Date)
    duty_title: Mapped[Optional[str]] = mapped_column(String(200))
    reason_for_change: Mapped[Optional[str]] = mapped_column(String(200))
    pcs_tdy_deployment: Mapped[Optional[str]] = mapped_column(String(50))
    country: Mapped[Optional[str]] = mapped_column(String(100))


# ---------------------------------------------------------------------------
# SECURITY / DRIVER / WEAPONS / CBRN
# ---------------------------------------------------------------------------

class SecurityDriverWeaponsCBRN(BaseModelMixin, Base):
    """
    Section F.
    """
    __tablename__ = "security_driver_weapons_cbrn"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    # SECURITY
    clearance_type: Mapped[Optional[str]] = mapped_column(String(50))
    investigation_date: Mapped[Optional[date]] = mapped_column(Date)
    clearance_expiration: Mapped[Optional[date]] = mapped_column(Date)

    # DRIVER
    civilian_license_exp: Mapped[Optional[date]] = mapped_column(Date)
    military_license: Mapped[Optional[str]] = mapped_column(String(50))
    vehicle_quals_ref: Mapped[Optional[str]] = mapped_column(Text)
    nvg_qualification: Mapped[Optional[bool]] = mapped_column()

    # WEAPONS / CBRN
    weapons_summary_ref: Mapped[Optional[str]] = mapped_column(Text)
    cbrn_quals_ref: Mapped[Optional[str]] = mapped_column(Text)


# ---------------------------------------------------------------------------
# DEPLOYMENTS
# ---------------------------------------------------------------------------

class DeploymentRecord(BaseModelMixin, Base):
    """
    Section G: Deployments.
    """
    __tablename__ = "deployment_records"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    country: Mapped[Optional[str]] = mapped_column(String(100))
    start_date: Mapped[Optional[date]] = mapped_column(Date)
    end_date: Mapped[Optional[date]] = mapped_column(Date)
    combat_zone_pay: Mapped[Optional[bool]] = mapped_column()
    campaign_credits: Mapped[Optional[str]] = mapped_column(Text)
    notes: Mapped[Optional[str]] = mapped_column(Text)
    dd214_ref: Mapped[Optional[str]] = mapped_column(Text)


# ---------------------------------------------------------------------------
# LANGUAGES
# ---------------------------------------------------------------------------

class LanguageRecord(BaseModelMixin, Base):
    """
    Section H: Languages.
    """
    __tablename__ = "language_records"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    language: Mapped[str] = mapped_column(String(50))
    dlpt_listening: Mapped[Optional[int]] = mapped_column(Integer)
    dlpt_reading: Mapped[Optional[int]] = mapped_column(Integer)
    dlpt_speaking: Mapped[Optional[int]] = mapped_column(Integer)
    dlpt_date: Mapped[Optional[date]] = mapped_column(Date)
    proficiency_pay: Mapped[Optional[bool]] = mapped_column()


# ---------------------------------------------------------------------------
# MEDICAL READINESS SNAPSHOT (READ-ONLY MIRRORS)
# ---------------------------------------------------------------------------

class MedicalReadinessSnapshot(BaseModelMixin, Base):
    """
    Section I: Mirror of MEDPROS, HR Metrics, Profiles, Fitness.

    No medical details stored here (PHI protection):
    - Only summary fields allowed.
    """
    __tablename__ = "medical_readiness_snapshot"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    pha_date: Mapped[Optional[date]] = mapped_column(Date)
    dental_class: Mapped[Optional[str]] = mapped_column(String(10))
    mrc: Mapped[Optional[str]] = mapped_column(String(10))
    immunization_summary: Mapped[Optional[str]] = mapped_column(Text)
    hiv_date: Mapped[Optional[date]] = mapped_column(Date)
    vision_date: Mapped[Optional[date]] = mapped_column(Date)
    hearing_date: Mapped[Optional[date]] = mapped_column(Date)
    profile_type: Mapped[Optional[str]] = mapped_column(String(50))


# ---------------------------------------------------------------------------
# PERSONAL / FAMILY DATA
# ---------------------------------------------------------------------------

class PersonalFamilyData(BaseModelMixin, Base):
    """
    Section J.
    """
    __tablename__ = "personal_family_data"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    marital_status: Mapped[Optional[str]] = mapped_column(String(50))
    dependents_ref: Mapped[Optional[str]] = mapped_column(Text)
    nok_ref: Mapped[Optional[str]] = mapped_column(Text)
    efmp_status: Mapped[Optional[str]] = mapped_column(String(50))
    family_care_plan: Mapped[Optional[str]] = mapped_column(String(200))
    bah_bas_status: Mapped[Optional[str]] = mapped_column(String(50))
    home_of_record: Mapped[Optional[str]] = mapped_column(String(200))
    spouse_military: Mapped[Optional[bool]] = mapped_column()


# ---------------------------------------------------------------------------
# ADDITIONAL SOLDIER DATA
# ---------------------------------------------------------------------------

class AdditionalSoldierData(BaseModelMixin, Base):
    """
    Section K.
    """
    __tablename__ = "additional_soldier_data"

    soldier_id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("soldiers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    gt_score: Mapped[Optional[int]] = mapped_column(Integer)
    asvab_ref: Mapped[Optional[str]] = mapped_column(Text)
    additional_duties_ref: Mapped[Optional[str]] = mapped_column(Text)
    certifications_ref: Mapped[Optional[str]] = mapped_column(Text)
    civilian_licenses_ref: Mapped[Optional[str]] = mapped_column(Text)
    equipment_keys_ref: Mapped[Optional[str]] = mapped_column(Text)
    access_badges_ref: Mapped[Optional[str]] = mapped_column(Text)
