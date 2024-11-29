import uuid

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Strategy
from core.schemas.strategy import StrategyInDB
from core.exceptions.db_exceptions import DatabaseException


class StrategyRepo:
    @staticmethod
    async def insert_strategy(strategy_in: StrategyInDB, session: AsyncSession):
        new_strategy = Strategy(**strategy_in.model_dump())
        session.add(new_strategy)
        await session.flush()
        await session.refresh(new_strategy)
        return new_strategy

    @staticmethod
    async def update_strategy(strategy_in: StrategyInDB, strategy_uuid: uuid.UUID, session: AsyncSession):
        stmt = select(Strategy).filter(Strategy.uuid == strategy_uuid)
        strategy = await session.execute(stmt)
        existing_strategy = strategy.scalar_one_or_none()

        if not existing_strategy:
            raise DatabaseException(msg=f'Strategy with UUID {strategy_uuid} not found.')

        for key, value in strategy_in.model_dump().items():
            setattr(existing_strategy, key, value)

        session.add(existing_strategy)
        await session.flush()
        await session.refresh(existing_strategy)

        return existing_strategy

    @staticmethod
    async def remove_strategy(strategy_uuid: uuid.UUID, session: AsyncSession):
        stmt = (
            delete(Strategy)
            .filter(Strategy.uuid == strategy_uuid)
            .returning(Strategy)
        )
        strategy = await session.scalar(stmt)
        if strategy is None:
            raise DatabaseException(msg="No file with this UUID")
        await session.flush()
        return strategy

    @staticmethod
    async def get_strategies_me(user_uuid: uuid.UUID, session: AsyncSession):
        result = await session.scalars(
            select(Strategy).filter(Strategy.user_uuid == user_uuid)
        )
        if result is None:
            raise DatabaseException(msg="You don't have strategies")
        return result
