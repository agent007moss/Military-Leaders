# app/modules/__init__.py

"""
Module registry.
Important: DO NOT import submodules here.
Importing modules here causes early model loading before main.py
calls init_models(), which breaks SQLAlchemy.
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
    "military_info",
]
