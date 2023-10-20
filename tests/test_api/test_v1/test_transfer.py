from fastapi.testclient import TestClient


def test_transfer(client_app: TestClient):
    resp = client_app.post(
        "/api/v1/transfer",
        json={
            "event": {
                "log": {
                    "invoice": {
                        "amount": 100,
                        "fee": 5,
                    }
                }
            }
        },
    )

    assert resp.status_code == 204


def test_transfer_without_amount(client_app: TestClient):
    resp = client_app.post(
        "/api/v1/transfer",
        json={
            "event": {
                "log": {
                    "invoice": {
                        "fee": 5,
                    }
                }
            }
        },
    )

    assert resp.status_code == 404
    assert resp.json() == {"detail": "Invoice not found"}
