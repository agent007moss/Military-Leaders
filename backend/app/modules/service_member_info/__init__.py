"""
Service Member Military Info Box (Master Personnel Record).

Loads all Master Personnel Record tables so SQLAlchemy creates them.
"""

from fastapi import APIRouter

# Force SQLAlchemy to import and register the models
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

# Create an EMPTY router so FastAPI can load it safely
router = APIRouter(
    prefix="/service-member-info",
    tags=["service_member_info"],
)

def get_router():
    return router

