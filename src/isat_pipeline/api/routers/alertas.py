from fastapi import APIRouter
from ..schemas import PredictionResponse
from ...ml.detector import load_model, predict

router = APIRouter()


@router.post("/realtime", response_model=PredictionResponse)
def realtime_alert(observation: dict) -> PredictionResponse:
    model = load_model()
    if model is None:
        return PredictionResponse(defect="no_defecto", confidence=0.0, alert="Modelo no disponible")

    prediction, confidence = predict(model, observation)
    alert = None
    if prediction != "no_defecto" and confidence >= 0.6:
        alert = f"Alerta crítica: {prediction} detectado con {confidence:.0%}"

    return PredictionResponse(defect=prediction, confidence=confidence, alert=alert)
