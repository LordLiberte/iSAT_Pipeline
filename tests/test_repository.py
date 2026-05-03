from datetime import datetime

from src.isat_pipeline.db.models import PieceEvent
from src.isat_pipeline.db.repository import save_events, list_recent_events, count_defects


def test_repository_crud() -> None:
    events = [
        PieceEvent(timestamp=datetime.utcnow(), machine_id="M-01", tool_wear=12.0, process_pressure=80.0, temperature=70.0, speed=1000.0, defect="no_defecto"),
        PieceEvent(timestamp=datetime.utcnow(), machine_id="M-02", tool_wear=40.0, process_pressure=110.0, temperature=90.0, speed=1200.0, defect="fisura"),
    ]
    save_events(events)
    recent = list_recent_events(limit=2)
    assert len(recent) >= 2
    assert count_defects() >= 1
