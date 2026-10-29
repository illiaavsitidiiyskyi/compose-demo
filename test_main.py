from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_hits_increase():
    first = client.get("/").json()["hits"]
    second = client.get("/").json()["hits"]
    assert second == first + 2
