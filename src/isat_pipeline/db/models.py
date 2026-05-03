from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field


class PieceEvent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: datetime
    machine_id: str
    tool_wear: float
    process_pressure: float
    temperature: float
    speed: float
    defect: str
