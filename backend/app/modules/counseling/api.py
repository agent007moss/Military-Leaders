from fastapi import APIRouter


def get_router() -> APIRouter:
    router = APIRouter()

    @router.get("/ping")
    async def ping() -> dict:
        return {"module": "counseling", "status": "ok"}

    return router
