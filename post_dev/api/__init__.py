from fastapi import APIRouter
from core.settings import settings
from .api_v1 import router as router_api_v1

router = APIRouter(
    prefix=settings.api.prefix,
)
router.include_router(
    router_api_v1,
)