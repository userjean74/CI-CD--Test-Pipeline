import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Welcome to the CI_CD_Test API",
        "project": "Automated Testing and Docker CI"
    }


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "healthy"
    }


def test_unknown_endpoint_returns_404(client):
    response = client.get("/unknown")

    assert response.status_code == 404
