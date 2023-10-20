from fastapi import APIRouter, Body, Depends

from src.domains.payment_processing import (
    STARK_BANK_ACCOUNT,
    PaymentProcessing,
)
from src.repository.payment_repository import PaymentRepositoryI, get_payment_repository


router = APIRouter()


@router.post("/transfer")
async def transfer(
    data: dict = Body(),
    sb: PaymentRepositoryI = Depends(get_payment_repository),
):
    amount = data.get("event", {}).get("log", {}).get("invoice", {}).get("amount", None)
    fee = data.get("event", {}).get("log", {}).get("invoice", {}).get("fee", None)
    if amount is None or fee is None:
        return 404

    payment = PaymentProcessing(
        account=STARK_BANK_ACCOUNT,
        amount=amount,
        fee=fee,
    )

    sb.transfer(payment=payment)

    return 200
