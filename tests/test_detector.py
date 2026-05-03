from src.isat_pipeline.ml.detector import train_model, load_model, predict


def test_train_and_predict() -> None:
    data = [
        {"tool_wear": 10.0, "process_pressure": 80.0, "temperature": 70.0, "speed": 1000.0, "defect": "no_defecto"},
        {"tool_wear": 35.0, "process_pressure": 110.0, "temperature": 90.0, "speed": 1200.0, "defect": "fisura"},
        {"tool_wear": 40.0, "process_pressure": 120.0, "temperature": 95.0, "speed": 1300.0, "defect": "soldadura_fria"},
        {"tool_wear": 12.0, "process_pressure": 65.0, "temperature": 68.0, "speed": 980.0, "defect": "no_defecto"},
    ]

    model, score = train_model(data)
    assert score >= 0.0

    loaded = load_model()
    assert loaded is not None

    prediction, confidence = predict(loaded, {"tool_wear": 40.0, "process_pressure": 115.0, "temperature": 92.0, "speed": 1240.0, "defect": "fisura"})
    assert isinstance(prediction, str)
    assert 0.0 <= confidence <= 1.0
