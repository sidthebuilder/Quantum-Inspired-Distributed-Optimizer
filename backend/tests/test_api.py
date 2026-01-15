from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Quantum-Inspired Optimizer API is running"}

def test_start_optimization():
    payload = {
        "iterations": 100,
        "temperature": 50.0,
        "cooling_rate": 0.8
    }
    response = client.post("/api/optimize", json=payload)
    
    # Note: In a real integration test without a running Redis, this might fail or stick in PENDING.
    # For unit testing the API layer, we mock celery, but here checking 202 Accepted is enough.
    assert response.status_code == 202
    data = response.json()
    assert "task_id" in data
    assert data["status"] == "Processing"
