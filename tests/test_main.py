from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "CI/CD pipeline is working"}


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_sum() -> None:
    response = client.get("/sum", params={"a": 10, "b": 15})
    assert response.status_code == 200
    assert response.json() == {"result": 25}
