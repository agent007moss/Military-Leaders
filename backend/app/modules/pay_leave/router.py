# app/modules/pay_leave/router.py

from fastapi import APIRouter

def get_router() -> APIRouter:
    router = APIRouter(
        prefix="/pay-leave",
        tags=["pay_leave"],
    )

    # Phase A: no endpoints yet
    return router
