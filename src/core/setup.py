from contextlib import asynccontextmanager
from typing import Any
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware


def lifespan_factory():
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        yield

    return lifespan


def create_application(router: APIRouter, **kwargs: Any) -> FastAPI:
    lifespan = lifespan_factory()
    application = FastAPI(lifespan=lifespan, **kwargs)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(router)
    return application
