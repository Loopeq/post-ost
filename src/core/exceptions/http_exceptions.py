from typing import Any

from fastapi import HTTPException


class BuildException(HTTPException):
    _name = "Build error"

    def __init__(self, detail: Any | None, status_code: int = 400):
        super().__init__(
            detail=f"{BuildException._name}: {detail}", status_code=status_code
        )
