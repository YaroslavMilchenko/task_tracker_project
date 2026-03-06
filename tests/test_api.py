from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Hello! FastAPI is successfully running."}

def test_create_task_unauthorized():
    response = client.post("/tasks/", json={"title": "Hack", "description": "Without token"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}