from uuid import UUID
from pydantic import BaseModel, Field


class BaseStrategy(BaseModel):
    name: str = Field(max_length=100)
    user_uuid: UUID


class StrategyOut(BaseModel):
    name: str = Field(max_length=100)
    uuid: UUID


class StrategyInDB(BaseStrategy):
    pass
