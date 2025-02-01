from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_project_info():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["project_description"] == "This is a simple API that provides information about a project."