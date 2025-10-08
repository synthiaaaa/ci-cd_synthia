from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_square():
    response = client.get("/square/4")
    assert response.status_code == 200
    assert response.json() == {"number": 4.0, "square": 16.0}


def test_sqrt():
    response = client.get("/sqrt/9")
    assert response.status_code == 200
    assert response.json() == {"number": 9.0, "sqrt": 3.0}


def test_sqrt_negative():
    response = client.get("/sqrt/-9")
    assert response.status_code == 400
