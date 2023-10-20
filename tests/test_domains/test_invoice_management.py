import pytest
from src.domains.invoice_management import Customer, Invoice


@pytest.fixture
def customer():
    customer = Customer(
        tax_id="123.456.789-09",
        name="John B. Doe",
    )
    assert customer.tax_id == "123.456.789-09"
    assert customer.name == "John B. Doe"
    return customer


def test_create_customer():
    customer = Customer(
        tax_id="123.456.789-09",
        name="John Titor",
    )
    assert customer.tax_id == "123.456.789-09"
    assert customer.name == "John Titor"


# pytest to catch errors
def test_create_customer_without_tax_id():
    with pytest.raises(ValueError) as excinfo:
        Customer(
            tax_id=None,
            name="John Doe",
        )
        assert str(excinfo.value) == "tax_id is required"

    with pytest.raises(ValueError) as excinfo:
        Customer(
            tax_id="",
            name="John Doe",
        )


def test_create_customer_with_invalid_tax_id():
    with pytest.raises(ValueError) as excinfo:
        Customer(
            tax_id="123.A56.789-09",
            name="John A. Doe",
        )
        assert str(excinfo.value) == "tax_id is invalid"


def test_create_customar_with_invalid_name():
    with pytest.raises(ValueError) as excinfo:
        Customer(
            tax_id="123.456.789-09",
            name=None,
        )
        assert str(excinfo.value) == "name is required"

    with pytest.raises(ValueError) as excinfo:
        Customer(
            tax_id="123.456.789-09",
            name="a",
        )
        assert str(excinfo.value) == "name is too short"

    with pytest.raises(ValueError) as excinfo:
        Customer(
            tax_id="123.456.789-09",
            name=123,
        )
        assert str(excinfo.value) == "name must be a string"


def test_random_customer():
    assert isinstance(Customer.random(), Customer)


def test_create_invoice(
    customer: Customer,
):
    invoice = Invoice(
        customer=customer,
        amount=100,
    )
    assert invoice.customer == customer
    assert invoice.amount == 100


def test_create_invoice_without_customer():
    with pytest.raises(ValueError) as excinfo:
        Invoice(
            customer=None,
            amount=100,
        )
        assert str(excinfo.value) == "customer is required"


def test_create_invoice_with_invalid_customer():
    with pytest.raises(ValueError) as excinfo:
        Invoice(
            customer="customer",
            amount=100,
        )
        assert str(excinfo.value) == "customer must be a Customer instance"


def test_create_invoice_with_invalid_amount():
    with pytest.raises(ValueError) as excinfo:
        Invoice(
            customer=Customer.random(),
            amount=None,
        )
        assert str(excinfo.value) == "amount is required"

    with pytest.raises(ValueError) as excinfo:
        Invoice(
            customer=Customer.random(),
            amount=-5,
        )
        assert str(excinfo.value) == "amount must be greater than zero"


def test_create_invoice_with_invalid_status():
    with pytest.raises(ValueError) as excinfo:
        Invoice(
            customer=Customer.random(),
            amount=100,
            status="status",
        )
        assert str(excinfo.value) == "status must be a InvoiceStatus instance"


def test_random_invoice():
    assert isinstance(Invoice.random(), Invoice)
