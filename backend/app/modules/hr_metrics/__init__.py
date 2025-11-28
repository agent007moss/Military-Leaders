# app/modules/hr_metrics/__init__.py

from .models import (
    HRMetricKind,
    HRMetricStatusColor,
    HRMetricDefinition,
    HRMetricEntry,
)

# Router stub (Phase A: models only, no endpoints yet)
# Must exist so app.core.router.include_all_routers does not fail.
def get_router():
    from fastapi import APIRouter
    router = APIRouter(prefix="/hr-metrics", tags=["HR Metrics"])
    return router


__all__ = [
    "HRMetricKind",
    "HRMetricStatusColor",
    "HRMetricDefinition",
    "HRMetricEntry",
    "get_router",
]

