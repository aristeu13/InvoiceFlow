from fastapi import APIRouter, Body
import starkbank

from src.domains.payment_processing import (
    STARK_BANK_ACCOUNT,
    PaymentProcessing,
)


router = APIRouter()


@router.post("/transfer")
async def transfer(
    data: dict = Body(),
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

    starkbank.transfer.create(
        [
            starkbank.Transfer(
                amount=payment.net_value,
                name=payment.account.name,
                tax_id=payment.account.tax_id,
                bank_code=payment.account.bank_code,
                branch_code=payment.account.branch,
                account_number=payment.account.account_number,
                account_type=payment.account.account_type,
            )
        ]
    )
    return 200
