from fastapi.testclient import TestClient
import pytest
from src.main import app


_client = TestClient(app)


@pytest.fixture
def client_app():
    return _client
