import pytest
from YaldaKarimi_simple_profile_flask import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Yalda" in response.data
