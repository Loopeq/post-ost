import uuid as uuid_pkg

from sqlalchemy.orm import Session
from src.core.models import User
from src.core.utils.utils import get_password_hash
from tests.conftest import fake


def create_user(
    db: Session,
    password: str,
    is_super_user: bool = False,
    disabled: bool = False,
) -> User:

    _user = User(
        username=fake.name(),
        email=fake.email(),
        password=get_password_hash(password=password),
        uuid=uuid_pkg.uuid4(),
        disabled=disabled,
        superuser=is_super_user,
    )
    db.add(_user)
    db.commit()
    db.refresh(_user)

    return _user
