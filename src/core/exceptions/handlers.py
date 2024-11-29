from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from core.exceptions.base import BoxException
from core.exceptions.http_exceptions import BuildException
from core.utils.utils import strip_error_msg


async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": strip_error_msg(str(exc))},
    )


exception_handlers: list[BoxException] = [
    BoxException(
        exception_handler=exception_handler, exception_class=BuildException
    )
]
