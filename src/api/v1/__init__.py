from fastapi.routing import APIRouter
from api.v1.users import router as user_router
from api.v1.login import router as login_router
from api.v1.strategy import router as strategy_router

router = APIRouter(prefix="/v1")

router.include_router(user_router)
router.include_router(login_router)
router.include_router(strategy_router)
