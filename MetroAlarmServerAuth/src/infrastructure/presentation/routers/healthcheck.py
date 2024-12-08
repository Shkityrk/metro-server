from fastapi import APIRouter

__all__ = [
    "healthcheck_router",
]


healthcheck_router = APIRouter()


@healthcheck_router.get("/auth/healthcheck")
async def healthcheck() -> str:
    return "ok"
