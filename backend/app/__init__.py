# app package marker
# app/modules/__init__.py

"""
Module registry loader.
We DO NOT import submodules here because it causes models.py to load
before Base.metadata.clear() runs in main.py.
"""

MODULES = [
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
    "military_info",   # ← imported later by router loader, NOT here
]
