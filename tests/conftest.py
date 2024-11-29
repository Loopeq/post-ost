from typing import Any, Generator, Callable
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from faker import Faker
from starlette.testclient import TestClient
from src.main import app
from src.core.settings import settings

DATABASE_URL = f"{settings.db.sync_prefix}{settings.db.user}:{settings.db.password}@{settings.db.server}:5432/{settings.db.db}"


sync_engine = create_engine(DATABASE_URL)
local_session = sessionmaker(
    autocommit=False, autoflush=False, bind=sync_engine
)

fake = Faker()


@pytest.fixture(scope="session")
def client() -> Generator[TestClient, Any, None]:
    with TestClient(app) as _client:
        yield _client
    app.dependency_overrides = {}
    sync_engine.dispose()


@pytest.fixture
def db() -> Generator[Session, Any, None]:
    session = local_session()
    yield session
    session.close()


def override_dependency(
    dependency: Callable[..., Any], mocked_response: Any
) -> None:
    app.dependency_overrides[dependency] = lambda: mocked_response
