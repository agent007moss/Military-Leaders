# main.py

from __future__ import annotations

# ---------------------------------------------------------
# ABSOLUTELY FIRST: clear SQLAlchemy metadata BEFORE
# any model imports (fixes "Table already defined" error)
# ---------------------------------------------------------
from app.core.db import Base, init_models, engine  # init_models imported early
Base.metadata.clear()
# ---------------------------------------------------------

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.router import include_all_routers
from app.core.settings import get_settings


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title="Military Leaders Tool - Backend",
        version="0.1.0",
        description="Fresh minimal backend skeleton (SQLite, FastAPI, SQLAlchemy 2.x).",
    )

    # -----------------------------------------------------
    # Create database tables AFTER metadata wipe
    # but BEFORE loading module routers (VERY IMPORTANT)
    # -----------------------------------------------------
    init_models()

    # CORS (unchanged)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routers load ONLY after tables exist
    include_all_routers(app)

    @app.get("/health", tags=["system"])
    async def health_check() -> dict:
        return {
            "status": "ok",
            "env": settings.environment,
            "db": settings.database_url,
        }

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
