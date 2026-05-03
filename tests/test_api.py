from fastapi.testclient import TestClient

from src.isat_pipeline.api.main import app
from src.isat_pipeline.ml.detector import train_model


def test_health_endpoint() -> None:
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_predict_endpoint() -> None:
    data = [
        {"tool_wear": 10.0, "process_pressure": 80.0, "temperature": 70.0, "speed": 1000.0, "defect": "no_defecto"},
        {"tool_wear": 40.0, "process_pressure": 110.0, "temperature": 90.0, "speed": 1200.0, "defect": "fisura"},
        {"tool_wear": 12.0, "process_pressure": 75.0, "temperature": 68.0, "speed": 980.0, "defect": "no_defecto"},
    ]
    train_model(data)

    client = TestClient(app)
    payload = {
        "timestamp": "2026-05-03T12:00:00",
        "machine_id": "M-03",
        "tool_wear": 38.0,
        "process_pressure": 115.0,
        "temperature": 92.0,
        "speed": 1250.0,
    }
    response = client.post("/piezas/predict", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "defect" in body
    assert "confidence" in body
