from pathlib import Path
from sqlmodel import SQLModel, create_engine, Session

from ..config import BASE_DIR

DB_PATH = BASE_DIR / "data" / "isat_pipeline.db"
ENGINE = create_engine(f"sqlite:///{DB_PATH}", echo=False, connect_args={"check_same_thread": False})


def init_db() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    SQLModel.metadata.create_all(ENGINE)


def get_session() -> Session:
    return Session(ENGINE)
