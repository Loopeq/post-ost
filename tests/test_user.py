import pytest
from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from core.models import User
from api.dependencies import get_current_user
from src.core.security.security import oauth2_scheme
from tests.conftest import override_dependency, fake
from tests.helpers import generator, mocks


@pytest.fixture
def create_and_delete_user(db: Session):
    fake_password = fake.password()
    user = generator.create_user(db, password=fake_password)

    yield user, fake_password

    db.delete(user)
    db.commit()


def test_get_user_me(
    db: Session, client: TestClient, create_and_delete_user: tuple[User, None]
) -> None:
    user, fake_password = create_and_delete_user
    override_dependency(get_current_user, mocks.get_current_user(user))
    override_dependency(oauth2_scheme, mocks.oauth2_scheme())

    login_response = client.post(
        "/v1/login",
        data={"username": user.username, "password": fake_password},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    assert login_response.status_code == status.HTTP_200_OK

    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get(f"/v1/users/me", headers=headers)

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()

    assert response_json["id"] == user.id
    assert response_json["uuid"] == str(user.uuid)
    assert response_json["email"] == user.email
    assert response_json["username"] == user.username
