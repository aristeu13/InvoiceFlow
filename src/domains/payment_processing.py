class Account:
    def __init__(
        self,
        bank_code: str,
        branch: str,
        account_number: str,
        name: str,
        tax_id: str,
        account_type: str,
    ) -> None:
        self.bank_code = bank_code
        self.branch = branch
        self.account_number = account_number
        self.name = name
        self.tax_id = tax_id
        self.account_type = account_type


STARK_BANK_ACCOUNT = Account(
    bank_code="20018183",
    branch="0001",
    account_number="6341320293482496",
    name="Stark Bank S.A.",
    tax_id="20.018.183/0001-80",
    account_type="payment",
)


class PaymentProcessing:
    def __init__(
        self,
        account: Account,
        amount: int,
        fee: int,
    ) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

        if fee < 0:
            raise ValueError("Fee must be greater than 0")

        if not isinstance(account, Account):
            raise TypeError("Account must be an instance of Account")

        self.account = account
        self.amount = amount
        self.fee = fee

    @property
    def net_value(self) -> int:
        return self.amount - self.fee
