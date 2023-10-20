from abc import ABC
from fastapi import Depends
import starkbank
from src.core.settings import Settings, get_settings

from src.domains.invoice_management import Invoice


class InvoiceRepositoryI(ABC):
    def __init__(self, sb):
        self.sb = sb

    def send(self, invoices: list[Invoice]):
        raise NotImplementedError


class InvoiceRepository(InvoiceRepositoryI):
    def __init__(self, sb):
        super().__init__(sb)

    def send(self, invoices: list[Invoice]):
        self.sb.invoice.create(
            [
                starkbank.Invoice(
                    amount=i.amount,
                    tax_id=i.customer.tax_id,
                    name=i.customer.name,
                )
                for i in invoices
            ]
        )


class InvoiceRepositoryMock(InvoiceRepositoryI):
    def __init__(self, sb):
        super().__init__(sb)

    def send(self, invoices: list[Invoice]):
        print("Mocked invoice")
        print(invoices)


def get_invoice_repository(
    settings: Settings = Depends(get_settings),
) -> InvoiceRepositoryI:
    user = starkbank.Project(
        environment=settings.sb_environment,
        id=settings.sb_project_id,
        private_key=settings.sb_private_key,
    )
    starkbank.user = user
    return InvoiceRepository(starkbank)
