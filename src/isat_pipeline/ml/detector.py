from pathlib import Path
from typing import Any, Dict, Tuple, Union
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

from ..config import MODEL_PATH
from ..parsing.protocolo_isat import extract_features


def create_pipeline() -> Pipeline:
    return Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", RandomForestClassifier(n_estimators=50, random_state=42))
    ])


def train_model(data: list[Dict[str, Any]]) -> Tuple[Pipeline, float]:
    X, y = extract_features(data)
    model = create_pipeline()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    score = float(accuracy_score(y_test, model.predict(X_test)))
    save_model(model)
    return model, score


def save_model(model: Pipeline) -> None:
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)


def load_model() -> Union[Pipeline, None]:
    if MODEL_PATH.exists():
        return joblib.load(MODEL_PATH)
    return None


def predict(model: Pipeline, observation: Union[Dict[str, Any], Any]) -> Tuple[str, float]:
    if isinstance(observation, dict):
        observation = observation
    else:
        observation = observation.dict()

    X, _ = extract_features([observation])
    proba = model.predict_proba(X)[0]
    labels = model.classes_
    best_idx = int(np.argmax(proba))
    return labels[best_idx], float(proba[best_idx])
