from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class HealthResponse(BaseModel):
    status: str
    environment: str


class PieceObservation(BaseModel):
    timestamp: datetime
    machine_id: str
    tool_wear: float
    process_pressure: float
    temperature: float
    speed: float


class PredictionResponse(BaseModel):
    defect: str
    confidence: float
    alert: Optional[str] = None
