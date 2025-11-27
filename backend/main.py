"""Phase 1 Backend Entry Point (placeholder only).

This file wires together the app skeleton, routers, and placeholder services.
No business logic, persistence, or security rules are implemented yet.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.settings import get_settings
from app.core.router import include_all_routers


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title="Military Leaders Tool - Phase 1 Skeleton",
        version="0.1.0",
        description="Backend scaffolding only. No business logic implemented.",
    )

    # CORS (placeholder; values should be configured later)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    include_all_routers(app)

    @app.get("/health", tags=["system"])
    async def health_check() -> dict:
        return {"status": "ok", "phase": "1-skeleton"}

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
