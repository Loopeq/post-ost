from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User
from core.schemas.user import UserInDB


class UserRepo:

    @staticmethod
    async def insert_user(user_in: UserInDB, session: AsyncSession):
        user = User(**user_in.model_dump())
        session.add(user)
        await session.commit()
        return user

    @staticmethod
    async def get_user_by_username(
        username: str, session: AsyncSession
    ) -> User | None:
        stmt = select(User).filter(User.username == username)
        user = await session.execute(stmt)
        return user.scalar_one_or_none()
