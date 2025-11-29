# app/modules/training/router.py

from fastapi import APIRouter

def get_router() -> APIRouter:
    """
    Phase 1 stub router for Training module.
    No endpoints are defined until Phase B.
    """
    router = APIRouter(prefix="/training", tags=["training"])
    return router
