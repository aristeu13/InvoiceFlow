from fastapi.testclient import TestClient
import pytest
from src.main import app
from src.repository.payment_repository import (
    PaymentRepositoryMock,
    get_payment_repository,
)


def override_get_payment_repository():
    any_object = {}
    return PaymentRepositoryMock(any_object)


app.dependency_overrides[get_payment_repository] = override_get_payment_repository

_client = TestClient(app)


@pytest.fixture
def client_app():
    return _client
