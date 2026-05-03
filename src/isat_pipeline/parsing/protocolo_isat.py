import csv
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple

from ..config import CSV_SCHEMA, RAW_DATA_DIR, PROCESSED_DATA_DIR


def load_raw_data(path: Path) -> List[Dict[str, Any]]:
    data = []
    with path.open("r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({
                "timestamp": row["timestamp"],
                "machine_id": row["machine_id"],
                "tool_wear": float(row["tool_wear"]),
                "process_pressure": float(row["process_pressure"]),
                "temperature": float(row["temperature"]),
                "speed": float(row["speed"]),
                "defect": row["defect"].strip() or "no_defecto",
            })
    return data


def clean_data(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    cleaned = []
    for row in rows:
        if row["tool_wear"] < 0 or row["process_pressure"] < 0 or row["speed"] <= 0:
            continue
        cleaned.append(row)
    return cleaned


def extract_features(rows: List[Dict[str, Any]]) -> Tuple[List[List[float]], List[str]]:
    X = []
    y = []
    for row in rows:
        X.append([
            row["tool_wear"],
            row["process_pressure"],
            row["temperature"],
            row["speed"],
        ])
        y.append(row.get("defect", "unknown"))
    return X, y


def save_processed(rows: List[Dict[str, Any]], filename: str = "processed.csv") -> Path:
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_path = PROCESSED_DATA_DIR / filename
    with output_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_SCHEMA)
        writer.writeheader()
        for row in rows:
            writer.writerow({
                **row,
                "timestamp": row["timestamp"],
            })
    return output_path
