from pathlib import Path
from typing import List, Dict, Any

from prefect import flow, task

from .parsing.protocolo_isat import load_raw_data, clean_data, save_processed
from .ml.detector import train_model
from .config import RAW_DATA_DIR


@task
def load_and_clean(raw_path: Path) -> List[Dict[str, Any]]:
    data = load_raw_data(raw_path)
    return clean_data(data)


@task
def train_pipeline(rows: List[Dict[str, Any]]) -> float:
    model, score = train_model(rows)
    return score


@flow(name="isat-etl-flow")
def run_pipeline(raw_filename: str = "data.csv") -> float:
    raw_path = RAW_DATA_DIR / raw_filename
    data = load_and_clean(raw_path)
    save_processed(data)
    score = train_pipeline(data)
    return score


if __name__ == "__main__":
    run_pipeline()
