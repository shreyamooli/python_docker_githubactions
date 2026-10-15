import pytest

from app.main import app


@pytest.fixture
def client():
    return app.test_client()


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}


def test_add(client):
    res = client.get("/add?a=2&b=3.5")
    assert res.status_code == 200
    assert res.get_json()["result"] == 5.5


def test_add_bad_input(client):
    res = client.get("/add?a=x&b=1")
    assert res.status_code == 400
