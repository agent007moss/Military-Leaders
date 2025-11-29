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
    Boolean,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models_base import BaseModel, Branch, Component


# ============================================================
# SECTION A – ADMINISTRATIVE DATA
# ============================================================

class AdminData(BaseModel):
    __tablename__ = "admin_data"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

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


# ============================================================
# SECTION B – SERVICE DATA
# ============================================================

class ServiceData(BaseModel):
    __tablename__ = "service_data"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
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


# ============================================================
# SECTION C1 – MILITARY EDUCATION
# ============================================================

class MilitaryEducation(BaseModel):
    __tablename__ = "military_education"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    course_name: Mapped[str] = mapped_column(String(200))
    start_date: Mapped[Optional[date]] = mapped_column(Date)
    end_date: Mapped[Optional[date]] = mapped_column(Date)
    resident: Mapped[Optional[bool]] = mapped_column(Boolean)
    certificate_ref: Mapped[Optional[str]] = mapped_column(Text)
    notes: Mapped[Optional[str]] = mapped_column(Text)


# ============================================================
# SECTION C2 – CIVILIAN EDUCATION
# ============================================================

class CivilianEducation(BaseModel):
    __tablename__ = "civilian_education"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    highest_degree: Mapped[Optional[str]] = mapped_column(String(100))
    major: Mapped[Optional[str]] = mapped_column(String(100))
    school_name: Mapped[Optional[str]] = mapped_column(String(200))
    completion_date: Mapped[Optional[date]] = mapped_column(Date)
    credits: Mapped[Optional[int]] = mapped_column(Integer)


# ============================================================
# SECTION D – AWARDS SUMMARY
# ============================================================

class AwardSummary(BaseModel):
    __tablename__ = "award_summary"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    award_type: Mapped[str] = mapped_column(String(50))
    count: Mapped[Optional[int]] = mapped_column(Integer)
    last_award_date: Mapped[Optional[date]] = mapped_column(Date)
    award_periods_ref: Mapped[Optional[str]] = mapped_column(Text)


# ============================================================
# SECTION E – ASSIGNMENT HISTORY
# ============================================================

class AssignmentHistory(BaseModel):
    __tablename__ = "assignment_history"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
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


# ============================================================
# SECTION F – SECURITY / DRIVER / WEAPONS / CBRN
# ============================================================

class SecurityDriverWeaponsCBRN(BaseModel):
    __tablename__ = "security_driver_weapons_cbrn"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
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
    nvg_qualification: Mapped[Optional[bool]] = mapped_column(Boolean)

    # WEAPONS / CBRN
    weapons_summary_ref: Mapped[Optional[str]] = mapped_column(Text)
    cbrn_quals_ref: Mapped[Optional[str]] = mapped_column(Text)


# ============================================================
# SECTION G – DEPLOYMENTS
# ============================================================

class DeploymentRecord(BaseModel):
    __tablename__ = "deployment_records"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    country: Mapped[Optional[str]] = mapped_column(String(100))
    start_date: Mapped[Optional[date]] = mapped_column(Date)
    end_date: Mapped[Optional[date]] = mapped_column(Date)
    combat_zone_pay: Mapped[Optional[bool]] = mapped_column(Boolean)
    campaign_credits: Mapped[Optional[str]] = mapped_column(Text)
    notes: Mapped[Optional[str]] = mapped_column(Text)
    dd214_ref: Mapped[Optional[str]] = mapped_column(Text)


# ============================================================
# SECTION H – LANGUAGE RECORDS
# ============================================================

class LanguageRecord(BaseModel):
    __tablename__ = "language_records"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    language: Mapped[str] = mapped_column(String(50))
    dlpt_listening: Mapped[Optional[int]] = mapped_column(Integer)
    dlpt_reading: Mapped[Optional[int]] = mapped_column(Integer)
    dlpt_speaking: Mapped[Optional[int]] = mapped_column(Integer)
    dlpt_date: Mapped[Optional[date]] = mapped_column(Date)
    proficiency_pay: Mapped[Optional[bool]] = mapped_column(Boolean)


# ============================================================
# SECTION I – MEDICAL READINESS SNAPSHOT (NO PHI)
# ============================================================

class MedicalReadinessSnapshot(BaseModel):
    __tablename__ = "medical_readiness_snapshot"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
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


# ============================================================
# SECTION J – PERSONAL / FAMILY DATA
# ============================================================

class PersonalFamilyData(BaseModel):
    __tablename__ = "personal_family_data"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
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
    spouse_military: Mapped[Optional[bool]] = mapped_column(Boolean)


# ============================================================
# SECTION K – ADDITIONAL SOLDIER DATA
# ============================================================

class AdditionalSoldierData(BaseModel):
    __tablename__ = "additional_soldier_data"

    service_member_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_members.id", ondelete="CASCADE"),
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
