from __future__ import annotations

from datetime import date
from uuid import UUID
from typing import Optional, List

from pydantic import BaseModel

from app.core.models_base import Branch, Component


# ---------------------------------------------------------------------------
# SECTION SCHEMAS
# ---------------------------------------------------------------------------

class AdminDataCreate(BaseModel):
    """
    Payload used to CREATE/UPDATE AdminData for a soldier.
    """
    soldier_id: UUID

    last_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_initial: Optional[str] = None
    rank: Optional[str] = None
    grade: Optional[str] = None
    dodid: Optional[str] = None
    ssn_last4: Optional[str] = None
    dob: Optional[date] = None
    gender: Optional[str] = None
    component: Optional[Component] = None
    branch: Optional[Branch] = None
    unit: Optional[str] = None
    uic_ruc_pas_opfac: Optional[str] = None
    duty_title: Optional[str] = None
    duty_location: Optional[str] = None
    security_clearance: Optional[str] = None
    clearance_date: Optional[date] = None
    marital_status: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email_mil: Optional[str] = None
    email_civ: Optional[str] = None
    pmos_afsc_rate: Optional[str] = None


class AdminDataRead(BaseModel):
    id: UUID
    soldier_id: UUID

    last_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_initial: Optional[str] = None
    rank: Optional[str] = None
    grade: Optional[str] = None
    dodid: Optional[str] = None
    ssn_last4: Optional[str] = None
    dob: Optional[date] = None
    gender: Optional[str] = None
    component: Optional[Component] = None
    branch: Optional[Branch] = None
    unit: Optional[str] = None
    uic_ruc_pas_opfac: Optional[str] = None
    duty_title: Optional[str] = None
    duty_location: Optional[str] = None
    security_clearance: Optional[str] = None
    clearance_date: Optional[date] = None
    marital_status: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email_mil: Optional[str] = None
    email_civ: Optional[str] = None
    pmos_afsc_rate: Optional[str] = None

    class Config:
        from_attributes = True


class ServiceDataRead(BaseModel):
    id: UUID
    soldier_id: UUID

    basd: Optional[date] = None
    pebd: Optional[date] = None
    diems: Optional[date] = None
    ets_eas_eaos_dos: Optional[date] = None
    tis_years: Optional[int] = None
    tig_years: Optional[int] = None
    pay_grade: Optional[str] = None
    promotion_eligibility: Optional[str] = None
    flag_status: Optional[str] = None
    component_status: Optional[str] = None

    class Config:
        from_attributes = True


class MilitaryEducationRead(BaseModel):
    id: UUID
    soldier_id: UUID

    course_name: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    resident: Optional[bool] = None
    certificate_ref: Optional[str] = None
    notes: Optional[str] = None

    class Config:
        from_attributes = True


class CivilianEducationRead(BaseModel):
    id: UUID
    soldier_id: UUID

    highest_degree: Optional[str] = None
    major: Optional[str] = None
    school_name: Optional[str] = None
    completion_date: Optional[date] = None
    credits: Optional[int] = None

    class Config:
        from_attributes = True


class AwardSummaryRead(BaseModel):
    id: UUID
    soldier_id: UUID

    award_type: str
    count: Optional[int] = None
    last_award_date: Optional[date] = None
    award_periods_ref: Optional[str] = None

    class Config:
        from_attributes = True


class AssignmentHistoryRead(BaseModel):
    id: UUID
    soldier_id: UUID

    unit: Optional[str] = None
    station: Optional[str] = None
    uic_ruc_pas_opfac: Optional[str] = None
    from_date: Optional[date] = None
    to_date: Optional[date] = None
    duty_title: Optional[str] = None
    reason_for_change: Optional[str] = None
    pcs_tdy_deployment: Optional[str] = None
    country: Optional[str] = None

    class Config:
        from_attributes = True


class SecurityDriverWeaponsCBRNRead(BaseModel):
    id: UUID
    soldier_id: UUID

    clearance_type: Optional[str] = None
    investigation_date: Optional[date] = None
    clearance_expiration: Optional[date] = None

    civilian_license_exp: Optional[date] = None
    military_license: Optional[str] = None
    vehicle_quals_ref: Optional[str] = None
    nvg_qualification: Optional[bool] = None

    weapons_summary_ref: Optional[str] = None
    cbrn_quals_ref: Optional[str] = None

    class Config:
        from_attributes = True


class DeploymentRecordRead(BaseModel):
    id: UUID
    soldier_id: UUID

    country: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    combat_zone_pay: Optional[bool] = None
    campaign_credits: Optional[str] = None
    notes: Optional[str] = None
    dd214_ref: Optional[str] = None

    class Config:
        from_attributes = True


class LanguageRecordRead(BaseModel):
    id: UUID
    soldier_id: UUID

    language: str
    dlpt_listening: Optional[int] = None
    dlpt_reading: Optional[int] = None
    dlpt_speaking: Optional[int] = None
    dlpt_date: Optional[date] = None
    proficiency_pay: Optional[bool] = None

    class Config:
        from_attributes = True


class MedicalReadinessSnapshotRead(BaseModel):
    id: UUID
    soldier_id: UUID

    pha_date: Optional[date] = None
    dental_class: Optional[str] = None
    mrc: Optional[str] = None
    immunization_summary: Optional[str] = None
    hiv_date: Optional[date] = None
    vision_date: Optional[date] = None
    hearing_date: Optional[date] = None
    profile_type: Optional[str] = None

    class Config:
        from_attributes = True


class PersonalFamilyDataRead(BaseModel):
    id: UUID
    soldier_id: UUID

    marital_status: Optional[str] = None
    dependents_ref: Optional[str] = None
    nok_ref: Optional[str] = None
    efmp_status: Optional[str] = None
    family_care_plan: Optional[str] = None
    bah_bas_status: Optional[str] = None
    home_of_record: Optional[str] = None
    spouse_military: Optional[bool] = None

    class Config:
        from_attributes = True


class AdditionalSoldierDataRead(BaseModel):
    id: UUID
    soldier_id: UUID

    gt_score: Optional[int] = None
    asvab_ref: Optional[str] = None
    additional_duties_ref: Optional[str] = None
    certifications_ref: Optional[str] = None
    civilian_licenses_ref: Optional[str] = None
    equipment_keys_ref: Optional[str] = None
    access_badges_ref: Optional[str] = None

    class Config:
        from_attributes = True


# ---------------------------------------------------------------------------
# UNIFIED BUNDLE
# ---------------------------------------------------------------------------

class MilitaryInfoBundle(BaseModel):
    """
    Unified Master Personnel Record for one service member.
    """

    soldier_id: UUID

    admin_data: Optional[AdminDataRead] = None
    service_data: Optional[ServiceDataRead] = None

    military_education: List[MilitaryEducationRead] = []
    civilian_education: List[CivilianEducationRead] = []
    awards: List[AwardSummaryRead] = []
    assignments: List[AssignmentHistoryRead] = []
    deployments: List[DeploymentRecordRead] = []
    languages: List[LanguageRecordRead] = []

    security_driver_weapons_cbrn: Optional[SecurityDriverWeaponsCBRNRead] = None
    medical_readiness: Optional[MedicalReadinessSnapshotRead] = None
    personal_family: Optional[PersonalFamilyDataRead] = None
    additional_data: Optional[AdditionalSoldierDataRead] = None
