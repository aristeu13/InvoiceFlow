from fastapi.testclient import TestClient


def test_main(client_app: TestClient):
    resp = client_app.get("/health")

    assert resp.status_code == 200
    assert resp.json() == {"message": "Hello World"}
