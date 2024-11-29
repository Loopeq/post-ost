from uuid import UUID
from pydantic import BaseModel, Field, EmailStr


class BaseUser(BaseModel):
    username: str = Field(max_length=100)
    email: EmailStr
    disabled: bool
    superuser: bool


class UserOut(BaseUser):
    id: int
    uuid: UUID


class UserInDB(BaseUser):
    hashed_password: str
