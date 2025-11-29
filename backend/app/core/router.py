# app/core/router.py

from fastapi import APIRouter
from app.modules import MODULES


def include_all_routers(app):
    for module in MODULES:
        if hasattr(module, "get_router"):
            router = module.get_router()
            app.include_router(router)
            print(f"[ROUTER] Loaded: {module.__name__}")
