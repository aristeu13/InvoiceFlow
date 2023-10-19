from decimal import Decimal
from enum import Enum
from random import randint

from src.core.common.fake_person import generate_cpf, generate_name
from src.core.common.validates import validate_cpf


class InvoiceStatus(Enum):
    CREATED = "created"
    CANCELED = "canceled"
    PAID = "paid"
    OVERDUE = "overdue"
    VOIDED = "voided"
    EXPIRED = "expired"


class Customer:
    def __init__(
        self,
        tax_id: str,
        name: str,
    ) -> None:
        if not tax_id:
            raise ValueError("tax_id is required")
        if validate_cpf(tax_id) is False:
            raise ValueError("tax_id is invalid")

        if not name:
            raise ValueError("name is required")
        if isinstance(name, str) is False:
            raise ValueError("name must be a string")
        if len(name) < 3:
            raise ValueError("name is too short")

        self.tax_id = tax_id
        self.name = name

    @classmethod
    def random(cls) -> "Customer":
        return cls(
            tax_id=generate_cpf(),
            name=generate_name(),
        )


class Invoice:
    def __init__(
        self,
        customer: Customer,
        amount: int,
        status: InvoiceStatus = InvoiceStatus.CREATED,
    ) -> None:
        if not customer:
            raise ValueError("customer is required")
        if not isinstance(customer, Customer):
            raise ValueError("customer must be a Customer instance")

        if not amount:
            raise ValueError("amount is required")
        if amount <= 0:
            raise ValueError("amount must be greater than zero")

        if not isinstance(status, InvoiceStatus):
            raise ValueError("status must be a InvoiceStatus instance")

        self.customer = customer
        self.amount = amount
        self.status = status

    @classmethod
    def random(cls) -> "Invoice":
        return cls(
            customer=Customer.random(),
            amount=randint(1, 1_000_000),
            status=InvoiceStatus.CREATED,
        )
