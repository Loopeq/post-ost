from typing import Annotated

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.v1.crud.strategy import StrategyRepo
from api.dependencies import CURRENT_ACTIVE_USER
from api.v1.strategy import router
from core.db.db_helper import db_helper
from core.schemas.strategy import StrategyOut
from core.exceptions.db_exceptions import DatabaseException


@router.get("/me", response_model=list[StrategyOut])
async def get_strategies_me(
    current_user: CURRENT_ACTIVE_USER,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    try:
        strategies = await StrategyRepo.get_strategies_me(
            user_uuid=current_user.uuid, session=session
        )
        return strategies
    except DatabaseException as e:
        raise HTTPException(status_code=400, detail=e.msg)
    except Exception:
        raise HTTPException(
            status_code=500, detail="Error while getting your strategies"
        )
