from typing import List
from sqlmodel import select
from .session import get_session, init_db
from .models import PieceEvent


def save_events(events: List[PieceEvent]) -> None:
    init_db()
    with get_session() as session:
        session.add_all(events)
        session.commit()


def list_recent_events(limit: int = 50) -> List[PieceEvent]:
    with get_session() as session:
        statement = select(PieceEvent).order_by(PieceEvent.timestamp.desc()).limit(limit)
        return session.exec(statement).all()


def count_defects() -> int:
    with get_session() as session:
        statement = select(PieceEvent).where(PieceEvent.defect != "no_defecto")
        return len(list(session.exec(statement)))
