"""Central place to register all module routers.

Each module exposes a get_router() function that returns an APIRouter.
This file imports and includes them on the FastAPI app instance.
"""

from fastapi import FastAPI

# Import get_router functions from each module here (placeholders).
# NOTE: Do not add business logic; only wiring stubs.

from app.modules import (
    auth,
    soldier_profile,
    dashboard,
    appointments,
    battle_calendar,
    family,
    medpros,
    hr_metrics,
    medical_profiles,
    physical_fitness,
    weapons,
    training,
    flags_ucmj,
    counseling,
    tasks,
    duty_roster,
    appointments_tracker,
    pay_leave,
    hand_receipt,
    equipment_responsible,
    awards,
    evaluations,
    rating_scheme,
    licenses,
    military_info,
)


def include_all_routers(app: FastAPI) -> None:
    """Attach all module routers to the FastAPI app.

    Routers are prefixed by their module name.
    """

    module_map = {
        "auth": auth.get_router,
        "soldier_profile": soldier_profile.get_router,
        "dashboard": dashboard.get_router,
        "appointments": appointments.get_router,
        "battle_calendar": battle_calendar.get_router,
        "family": family.get_router,
        "medpros": medpros.get_router,
        "hr_metrics": hr_metrics.get_router,
        "medical_profiles": medical_profiles.get_router,
        "physical_fitness": physical_fitness.get_router,
        "weapons": weapons.get_router,
        "training": training.get_router,
        "flags_ucmj": flags_ucmj.get_router,
        "counseling": counseling.get_router,
        "tasks": tasks.get_router,
        "duty_roster": duty_roster.get_router,
        "appointments_tracker": appointments_tracker.get_router,
        "pay_leave": pay_leave.get_router,
        "hand_receipt": hand_receipt.get_router,
        "equipment_responsible": equipment_responsible.get_router,
        "awards": awards.get_router,
        "evaluations": evaluations.get_router,
        "rating_scheme": rating_scheme.get_router,
        "licenses": licenses.get_router,
        "military_info": military_info.get_router,
    }

    for prefix, get_router in module_map.items():
        try:
            app.include_router(get_router(), prefix=f"/api/{prefix}", tags=[prefix])
        except Exception:
            # Modules are allowed to be empty/placeholder in Phase 1 scaffold.
            continue
