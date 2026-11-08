from fastapi.testclient import TestClient
from api.main import app, model_service

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_generate_returns_503_when_model_not_loaded():
    original = model_service.generator
    model_service.generator = None
    try:
        response = client.post("/generate", json={"prompt": "Hello"})
        assert response.status_code == 503
        assert "Model is not loaded" in response.json()["detail"]
    finally:
        model_service.generator = original

def test_generate_request_validation():
    response = client.post("/generate", json={"prompt": "", "max_new_tokens": 0})
    assert response.status_code == 422
