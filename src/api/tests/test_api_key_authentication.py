from fastapi.testclient import TestClient


from app.main import app


client = TestClient(app)


def test_get_api_key_header():
    response = client.get("/v1/users/me",
                          headers={"X-API-Key": "fake_key", })
    assert response.status_code == 403
    assert response.json() == {"detail": "Could not validate credentials"}
