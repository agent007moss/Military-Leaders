"""
Service Member Military Info Box (Master Personnel Record).

Exports the unified ERB/STP-style master record tables:
- AdminData
- ServiceData
- MilitaryEducation
- CivilianEducation
- AwardSummary
- AssignmentHistory
- SecurityDriverWeaponsCBRN
- DeploymentRecord
- LanguageRecord
- MedicalReadinessSnapshot
- PersonalFamilyData
- AdditionalSoldierData
"""

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

__all__ = [
    "AdminData",
    "ServiceData",
    "MilitaryEducation",
    "CivilianEducation",
    "AwardSummary",
    "AssignmentHistory",
    "SecurityDriverWeaponsCBRN",
    "DeploymentRecord",
    "LanguageRecord",
    "MedicalReadinessSnapshot",
    "PersonalFamilyData",
    "AdditionalSoldierData",
]
