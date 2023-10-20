from fastapi import Request
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse
import logging


async def request_validation_exception_handler(request: Request, exception: Exception):
    if not isinstance(exception, RequestValidationError):
        return exception
    errors = exception.errors()
    logging.warning({"url": request.url.path, "errors": errors, "body": exception.body})

    first_error = errors[0]

    return JSONResponse(status_code=422, content=first_error)
