from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from api import router as api_router
from contextlib import asynccontextmanager
from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()


app = FastAPI(
    lifespan=lifespan,
    default_response_class=ORJSONResponse
)
app.include_router(api_router)


