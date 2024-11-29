from typing import Annotated
import jwt
from fastapi import Depends, status, HTTPException
from jwt import InvalidTokenError
from sqlalchemy.ext.asyncio import AsyncSession
from api.v1.crud.user import UserRepo
from core.db.db_helper import db_helper
from core.schemas.token import TokenData
from core.schemas.user import UserOut
from core.security.security import oauth2_scheme, SECRET_KEY, ALGORITHM


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = await UserRepo.get_user_by_username(
        username=token_data.username, session=session
    )
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[UserOut, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


CURRENT_USER = Annotated[UserOut, Depends(get_current_user)]
CURRENT_ACTIVE_USER = Annotated[UserOut, Depends(get_current_active_user)]
