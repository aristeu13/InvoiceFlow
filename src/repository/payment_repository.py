from abc import ABC

from fastapi import Depends
from src.core.settings import Settings, get_settings
from src.domains.payment_processing import PaymentProcessing
import starkbank


class PaymentRepositoryI(ABC):
    def __init__(self, sb):
        self.sb = sb

    def transfer(self, payment: PaymentProcessing):
        raise NotImplementedError


class PaymentRepository(PaymentRepositoryI):
    def __init__(self, sb):
        super().__init__(sb)

    def transfer(self, payment: PaymentProcessing):
        self.sb.transfer.create(
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


class PaymentRepositoryMock(PaymentRepositoryI):
    def __init__(self, sb):
        super().__init__(sb)

    def transfer(self, payment: PaymentProcessing):
        print("Mocked transfer")
        print(payment.net_value)
        print(payment.account.name)
        print(payment.account.tax_id)
        print(payment.account.bank_code)
        print(payment.account.branch)
        print(payment.account.account_number)
        print(payment.account.account_type)


def get_payment_repository(
    settings: Settings = Depends(get_settings),
) -> PaymentRepositoryI:
    user = starkbank.Project(
        environment=settings.SB_ENVIRONMENT,
        id=settings.SB_PROJECT_ID,
        private_key=settings.SB_PRIVATE_KEY,
    )

    starkbank.user = user

    return PaymentRepository(starkbank)
