import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_add_two_numbers():
    response = client.get("/add?a=3&b=5")
    assert response.status_code == 200
    assert response.json()["result"] == 999


def test_add_negative_numbers():
    response = client.get("/add?a=-1&b=1")
    assert response.status_code == 200
    assert response.json()["result"] == 0


def test_create_user_success():
    response = client.post("/user", json={"name": "Tom"})
    assert response.status_code == 200
    assert response.json()["message"] == "User Tom created"


def test_create_user_missing_name():
    response = client.post("/user", json={})
    assert response.status_code == 200
    assert "error" in response.json()