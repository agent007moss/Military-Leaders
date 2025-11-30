# app/modules/military_info/api.py

from __future__ import annotations

from datetime import date
from typing import Optional, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.security import get_current_user
from app.modules.soldier_profile.models import ServiceMember
from app.core.models_base import Branch, Component

from .models import (
    AdminData,
    ServiceData,
    MilitaryEducation,
    CivilianEducation,
    AwardSummary,
    AssignmentHistory,
    SecurityDriverWeaponsCBRN,
    DeploymentRecord,
    LanguageRecord,
    MedicalReadinessSnapshot,
    PersonalFamilyData,
    AdditionalSoldierData,
)
from .schemas import (
    MilitaryInfoBundle,
    AdminDataRead,
    ServiceDataRead,
    MilitaryEducationRead,
    CivilianEducationRead,
    AwardSummaryRead,
    AssignmentHistoryRead,
    SecurityDriverWeaponsCBRNRead,
    DeploymentRecordRead,
    LanguageRecordRead,
    MedicalReadinessSnapshotRead,
    PersonalFamilyDataRead,
    AdditionalSoldierDataRead,
)

router = APIRouter(
    prefix="/api/military-info",
    tags=["military_info"],
)

# ---------------------------------------------------------------------------
# INTERNAL HELPERS
# ---------------------------------------------------------------------------


def _get_single_or_none(model, soldier_id: UUID, db: Session):
    return (
        db.query(model)
        .filter(model.soldier_id == soldier_id)
        .order_by(model.created_at.asc())
        .first()
    )


def _get_many(model, soldier_id: UUID, db: Session):
    return (
        db.query(model)
        .filter(model.soldier_id == soldier_id)
        .order_by(model.created_at.asc())
        .all()
    )


# ---------------------------------------------------------------------------
# CREATE / UPDATE SCHEMAS (LOCAL TO THIS FILE)
# ---------------------------------------------------------------------------

class AdminDataCreate(BaseModel):
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


class AdminDataUpdate(BaseModel):
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


class ServiceDataCreate(BaseModel):
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


class ServiceDataUpdate(BaseModel):
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


# ---------------------------------------------------------------------------
# ADMIN DATA CRUD
# ---------------------------------------------------------------------------


@router.post(
    "/admin-data",
    response_model=AdminDataRead,
    status_code=status.HTTP_201_CREATED,
)
def create_admin_data(
    payload: AdminDataCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    # Optional: enforce that soldier exists
    soldier = (
        db.query(ServiceMember)
        .filter(ServiceMember.id == payload.soldier_id)
        .first()
    )
    if not soldier:
        raise HTTPException(status_code=404, detail="Service member not found")

    obj = AdminData(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.get(
    "/admin-data/{admin_id}",
    response_model=AdminDataRead,
)
def get_admin_data(
    admin_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    obj = db.query(AdminData).filter(AdminData.id == admin_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Admin data not found")
    return obj


@router.get(
    "/admin-data/by-soldier/{soldier_id}",
    response_model=List[AdminDataRead],
)
def list_admin_data_for_soldier(
    soldier_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    rows = (
        db.query(AdminData)
        .filter(AdminData.soldier_id == soldier_id)
        .order_by(AdminData.created_at.asc())
        .all()
    )
    return rows


@router.patch(
    "/admin-data/{admin_id}",
    response_model=AdminDataRead,
)
def update_admin_data(
    admin_id: UUID,
    payload: AdminDataUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    obj = db.query(AdminData).filter(AdminData.id == admin_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Admin data not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(obj, field, value)

    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete(
    "/admin-data/{admin_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_admin_data(
    admin_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    obj = db.query(AdminData).filter(AdminData.id == admin_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Admin data not found")

    db.delete(obj)
    db.commit()
    return None


# ---------------------------------------------------------------------------
# SERVICE DATA CRUD
# ---------------------------------------------------------------------------


@router.post(
    "/service-data",
    response_model=ServiceDataRead,
    status_code=status.HTTP_201_CREATED,
)
def create_service_data(
    payload: ServiceDataCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    soldier = (
        db.query(ServiceMember)
        .filter(ServiceMember.id == payload.soldier_id)
        .first()
    )
    if not soldier:
        raise HTTPException(status_code=404, detail="Service member not found")

    obj = ServiceData(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.get(
    "/service-data/{service_id}",
    response_model=ServiceDataRead,
)
def get_service_data(
    service_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    obj = db.query(ServiceData).filter(ServiceData.id == service_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Service data not found")
    return obj


@router.get(
    "/service-data/by-soldier/{soldier_id}",
    response_model=List[ServiceDataRead],
)
def list_service_data_for_soldier(
    soldier_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    rows = (
        db.query(ServiceData)
        .filter(ServiceData.soldier_id == soldier_id)
        .order_by(ServiceData.created_at.asc())
        .all()
    )
    return rows


@router.patch(
    "/service-data/{service_id}",
    response_model=ServiceDataRead,
)
def update_service_data(
    service_id: UUID,
    payload: ServiceDataUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    obj = db.query(ServiceData).filter(ServiceData.id == service_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Service data not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(obj, field, value)

    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete(
    "/service-data/{service_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_service_data(
    service_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    obj = db.query(ServiceData).filter(ServiceData.id == service_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Service data not found")

    db.delete(obj)
    db.commit()
    return None


# ---------------------------------------------------------------------------
# UNIFIED READ-ONLY BUNDLE
# ---------------------------------------------------------------------------


@router.get(
    "/{service_member_id}",
    response_model=MilitaryInfoBundle,
)
def get_military_info_bundle(
    service_member_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Unified read-only endpoint that returns the full Military Info Box
    (ERB/STP master record) for a single service member.
    """

    service_member = (
        db.query(ServiceMember)
        .filter(ServiceMember.id == service_member_id)
        .first()
    )
    if not service_member:
        raise HTTPException(status_code=404, detail="Service member not found")

    # TODO: enforce ownership/sharing later
    # if service_member.owner_user_id != current_user.id:
    #     raise HTTPException(status_code=403, detail="Not authorized")

    admin_obj = _get_single_or_none(AdminData, service_member_id, db)
    service_obj = _get_single_or_none(ServiceData, service_member_id, db)
    security_obj = _get_single_or_none(SecurityDriverWeaponsCBRN, service_member_id, db)
    medical_obj = _get_single_or_none(MedicalReadinessSnapshot, service_member_id, db)
    personal_obj = _get_single_or_none(PersonalFamilyData, service_member_id, db)
    additional_obj = _get_single_or_none(AdditionalSoldierData, service_member_id, db)

    mil_ed_list = _get_many(MilitaryEducation, service_member_id, db)
    civ_ed_list = _get_many(CivilianEducation, service_member_id, db)
    awards_list = _get_many(AwardSummary, service_member_id, db)
    assign_list = _get_many(AssignmentHistory, service_member_id, db)
    deploy_list = _get_many(DeploymentRecord, service_member_id, db)
    lang_list = _get_many(LanguageRecord, service_member_id, db)

    bundle = MilitaryInfoBundle(
        soldier_id=service_member_id,
        admin_data=AdminDataRead.model_validate(admin_obj) if admin_obj else None,
        service_data=ServiceDataRead.model_validate(service_obj) if service_obj else None,
        military_education=[
            MilitaryEducationRead.model_validate(obj) for obj in mil_ed_list
        ],
        civilian_education=[
            CivilianEducationRead.model_validate(obj) for obj in civ_ed_list
        ],
        awards=[
            AwardSummaryRead.model_validate(obj) for obj in awards_list
        ],
        assignments=[
            AssignmentHistoryRead.model_validate(obj) for obj in assign_list
        ],
        deployments=[
            DeploymentRecordRead.model_validate(obj) for obj in deploy_list
        ],
        languages=[
            LanguageRecordRead.model_validate(obj) for obj in lang_list
        ],
        security_driver_weapons_cbrn=(
            SecurityDriverWeaponsCBRNRead.model_validate(security_obj)
            if security_obj
            else None
        ),
        medical_readiness=(
            MedicalReadinessSnapshotRead.model_validate(medical_obj)
            if medical_obj
            else None
        ),
        personal_family=(
            PersonalFamilyDataRead.model_validate(personal_obj)
            if personal_obj
            else None
        ),
        additional_data=(
            AdditionalSoldierDataRead.model_validate(additional_obj)
            if additional_obj
            else None
        ),
    )

    return bundle


def get_router() -> APIRouter:
    return router
