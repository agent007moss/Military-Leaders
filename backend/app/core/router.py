# app/core/router.py

from fastapi import APIRouter
from importlib import import_module
from app.modules import MODULES


def include_all_routers(app):
    for name in MODULES:
        module_path = f"app.modules.{name}.api"
        try:
            api_module = import_module(module_path)
        except ModuleNotFoundError:
            continue

        if not hasattr(api_module, "get_router"):
            continue

        router = api_module.get_router()
        app.include_router(router)
