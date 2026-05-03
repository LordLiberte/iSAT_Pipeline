from fastapi import APIRouter, HTTPException
from ..schemas import PieceObservation, PredictionResponse
from ...ml.detector import load_model, predict

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def detect_defect(observation: PieceObservation) -> PredictionResponse:
    model = load_model()
    if model is None:
        raise HTTPException(status_code=503, detail="Modelo no disponible")

    prediction, confidence = predict(model, observation)
    alert = None
    if prediction != "no_defecto" and confidence >= 0.6:
        alert = f"Alerta: posible {prediction} con {confidence:.0%} de confianza"

    return PredictionResponse(defect=prediction, confidence=confidence, alert=alert)
