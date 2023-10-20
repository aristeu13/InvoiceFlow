from fastapi import APIRouter

from .v1.transfer import router as v1_transfer

router = APIRouter()

router.include_router(v1_transfer)
