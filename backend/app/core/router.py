from __future__ import annotations

from fastapi import FastAPI

from app import modules


MODULE_NAMES = [
    "auth",
    "soldier_profile",
    "dashboard",
    "appointments",
    "battle_calendar",
    "family",
    "medpros",
    "hr_metrics",
    "medical_profiles",
    "physical_fitness",
    "weapons",
    "training",
    "flags_ucmj",
    "counseling",
    "tasking",
    "duty_roster",
    "appointments_tracker",
    "pay_leave",
    "hand_receipt",
    "equipment_responsible",
    "awards",
    "evaluations",
    "rating_scheme",
    "licenses",
    "military_info",
    "perstats",
]


def include_all_routers(app: FastAPI) -> None:
    for name in MODULE_NAMES:
        module = getattr(modules, name, None)
        if module is None:
            continue

        get_router = getattr(module, "get_router", None)
        if get_router is None:
            continue

        router = get_router()
        prefix = f"/api/{name}"
        app.include_router(router, prefix=prefix, tags=[name])
        print(f"[ROUTER] attached: {name} -> {prefix}")
