from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
import starkbank
from src.api.api_v1 import router as router_v1
from src.core.settings import settings

from src.core.common.error_handler import request_validation_exception_handler

user = starkbank.Project(
    environment=settings.SB_ENVIRONMENT,
    id=settings.SB_PROJECT_ID,
    private_key=settings.SB_PRIVATE_KEY,
)

starkbank.user = user


app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return await request_validation_exception_handler(request=request, exception=exc)


@app.get("/health")
async def root():
    return {"message": "Hello World"}


app.include_router(router_v1, prefix="/api/v1")
