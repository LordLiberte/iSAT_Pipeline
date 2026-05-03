from pathlib import Path
import csv

from src.isat_pipeline.parsing.protocolo_isat import load_raw_data, clean_data, extract_features


def test_load_and_clean_data(tmp_path: Path) -> None:
    path = tmp_path / "sample.csv"
    rows = [
        {"timestamp": "2026-05-03T00:00:00", "machine_id": "M-01", "tool_wear": "10.0", "process_pressure": "80.0", "temperature": "70.0", "speed": "1000.0", "defect": "no_defecto"},
        {"timestamp": "2026-05-03T00:10:00", "machine_id": "M-02", "tool_wear": "-1.0", "process_pressure": "70.0", "temperature": "65.0", "speed": "900.0", "defect": "no_defecto"},
    ]
    with path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["timestamp", "machine_id", "tool_wear", "process_pressure", "temperature", "speed", "defect"])
        writer.writeheader()
        writer.writerows(rows)

    loaded = load_raw_data(path)
    assert len(loaded) == 2
    cleaned = clean_data(loaded)
    assert len(cleaned) == 1
    X, y = extract_features(cleaned)
    assert X[0] == [10.0, 80.0, 70.0, 1000.0]
    assert y[0] == "no_defecto"
