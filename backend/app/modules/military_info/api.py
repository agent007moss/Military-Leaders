# app/modules/military_info/api.py

from __future__ import annotations

from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.security import get_current_user
from app.modules.soldier_profile.models import ServiceMember

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

    # 1) Ensure service member exists
    service_member: Optional[ServiceMember] = (
        db.query(ServiceMember)
        .filter(ServiceMember.id == service_member_id)
        .first()
    )

    if not service_member:
        raise HTTPException(status_code=404, detail="Service member not found")

    # TODO: Enforce ownership / sharing model later:
    # if service_member.owner_user_id != current_user.id:
    #     raise HTTPException(status_code=403, detail="Not authorized")

    # 2) Fetch each section
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

    # 3) Build bundle, using Pydantic's from_attributes
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
