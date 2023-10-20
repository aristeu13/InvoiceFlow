import pytest
from src.domains.payment_processing import Account, PaymentProcessing


@pytest.fixture
def account():
    account = Account(
        bank_code="20018183",
        branch="0001",
        account_number="6341320293482496",
        name="Stark Bank S.A.",
        tax_id="20.018.183/0001-80",
        account_type="payment",
    )
    assert account.bank_code == "20018183"
    assert account.branch == "0001"
    assert account.account_number == "6341320293482496"
    assert account.name == "Stark Bank S.A."
    assert account.tax_id == "20.018.183/0001-80"
    assert account.account_type == "payment"
    return account


def test_payment_processing(account: Account):
    payment = PaymentProcessing(
        account=account,
        amount=100,
        fee=10,
    )
    assert payment.account == account
    assert payment.amount == 100
    assert payment.fee == 10
    assert payment.net_value == 90


def test_payment_processing_with_errors(account: Account):
    with pytest.raises(ValueError) as excinfo:
        PaymentProcessing(
            account=account,
            amount=0,
            fee=10,
        )
    assert "Amount must be greater than 0" in str(excinfo.value)
    with pytest.raises(ValueError) as excinfo:
        PaymentProcessing(
            account=account,
            amount=100,
            fee=-1,
        )
    assert "Fee must be greater than 0" in str(excinfo.value)
    with pytest.raises(TypeError) as excinfo:
        PaymentProcessing(
            account="account",  # type: ignore
            amount=100,
            fee=10,
        )
    assert "Account must be an instance of Account" in str(excinfo.value)
