import argparse
from datetime import datetime, timedelta
from pathlib import Path
import random
import csv

from src.isat_pipeline.config import RAW_DATA_DIR, CSV_SCHEMA


def generate_row(timestamp):
    wear = round(max(0.0, random.gauss(15, 5)), 2)
    pressure = round(max(0.0, random.gauss(80, 10)), 2)
    temperature = round(max(20.0, random.gauss(68, 8)), 2)
    speed = round(max(10.0, random.gauss(1050, 150)), 2)
    defect = "no_defecto"
    if wear > 25 or pressure > 95 or temperature > 80:
        defect = random.choice(["soldadura_fria", "fisura", "desalineacion"])
    return {
        "timestamp": timestamp.isoformat(),
        "machine_id": f"M-{random.randint(1, 5):02d}",
        "tool_wear": wear,
        "process_pressure": pressure,
        "temperature": temperature,
        "speed": speed,
        "defect": defect,
    }


def main(n: int, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    path = output / "data.csv"
    start = datetime.utcnow() - timedelta(days=7)
    with path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_SCHEMA)
        writer.writeheader()
        for i in range(n):
            row = generate_row(start + timedelta(minutes=i * 10))
            writer.writerow(row)
    print(f"Generado {n} filas en {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generador sintético de datos iSAT.")
    parser.add_argument("--n", type=int, default=5000, help="Número de registros a generar")
    parser.add_argument("--output", type=Path, default=RAW_DATA_DIR, help="Directorio de salida")
    args = parser.parse_args()
    main(args.n, args.output)
