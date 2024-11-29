from typing import Type
from pydantic import BaseModel
from starlette.types import ExceptionHandler


class BoxException(BaseModel):
    exception_handler: ExceptionHandler
    exception_class: int | Type[Exception]
