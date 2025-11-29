# dev_test.py
"""
Simple backend import test to ensure all core modules load without errors.
Does NOT touch the database. Used only for wiring validation.
"""

from app.core.db import engine, Base
from app.modules.soldier_profile.models import ServiceMember


def main():
    print("Engine:", engine)
    print("Base:", Base)
    print("Model OK:", ServiceMember.__tablename__)


if __name__ == "__main__":
    main()
