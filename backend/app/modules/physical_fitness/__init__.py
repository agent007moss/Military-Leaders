# app/modules/physical_fitness/__init__.py

from .models import (
    FitnessTestType,
    FitnessStatusColor,
    PhysicalFitnessTest,
)

# Phase A router stub – prevents import errors until API endpoints exist
def get_router():
    from fastapi import APIRouter
    router = APIRouter(prefix="/physical-fitness", tags=["Physical Fitness"])
    return router


__all__ = [
    "FitnessTestType",
    "FitnessStatusColor",
    "PhysicalFitnessTest",
    "get_router",
]

