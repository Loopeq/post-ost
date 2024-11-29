from datetime import datetime, timezone, timedelta

import jwt
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from core.utils.utils import verify_password
from core.settings import settings
from api.v1.crud.user import UserRepo

SECRET_KEY = settings.auth.secret
ALGORITHM = settings.auth.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.auth.expire_token_minute


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/login/")


async def authenticate_user(
    username: str, password: str, session: AsyncSession
):
    user = await UserRepo.get_user_by_username(username, session)
    if user is None:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    now = datetime.now(timezone.utc)
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=10)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
