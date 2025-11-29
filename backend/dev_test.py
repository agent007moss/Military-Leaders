"""Quick DB sanity test.

- Imports engine and Base
- Imports the core models we care about
- Creates all tables and prints basic info
"""

from app.core.db import engine, Base
from app.modules.auth.models import UserAccount
from app.modules.soldier_profile.models import ServiceMember


def main() -> None:
    print("Engine:", engine)
    print("Base:", Base)
    Base.metadata.create_all(bind=engine)
    print("Tables:", Base.metadata.tables.keys())
    print("OK: metadata and tables created.")


if __name__ == "__main__":
    main()
