import streamlit as st
from datetime import datetime
from pathlib import Path
import pandas as pd
import joblib

from src.isat_pipeline.config import PROCESSED_DATA_DIR, MODEL_PATH
from src.isat_pipeline.ml.detector import load_model, predict


st.set_page_config(page_title="iSAT Pipeline Dashboard", layout="wide")

st.title("iSAT Pipeline — Monitorización de calidad de piezas")

processed_file = PROCESSED_DATA_DIR / "processed.csv"
model = joblib.load('models/isat_detector.joblib')

if processed_file.exists():
    df = pd.read_csv(processed_file, parse_dates=["timestamp"])
    st.subheader("Datos procesados")
    st.dataframe(df.head(10))
    st.metric("Registros procesados", len(df))
    defect_rate = round((df["defect"] != "no_defecto").mean() * 100, 2)
    st.metric("Tasa de defectos", f"{defect_rate}%")
    st.line_chart(df.set_index("timestamp")["temperature"])
else:
    st.warning("No se encuentra datos procesados. Ejecuta el flujo ETL primero.")

st.subheader("Predicción rápida")
with st.form("prediction_form"):
    tool_wear = st.slider("Desgaste de herramienta", 0.0, 60.0, 15.0)
    process_pressure = st.slider("Presión de proceso", 0.0, 140.0, 80.0)
    temperature = st.slider("Temperatura", 20.0, 120.0, 68.0)
    speed = st.slider("Velocidad", 0.0, 1600.0, 1050.0)
    submitted = st.form_submit_button("Predecir defecto")

if submitted:
    if model is None:
        st.error("Modelo no disponible. Entrena el modelo con el flujo Prefect.")
    else:
        observation = {
            "tool_wear": tool_wear,
            "process_pressure": process_pressure,
            "temperature": temperature,
            "speed": speed,
        }
        prediction, confidence = predict(model, observation)
        st.write(f"### Resultado: {prediction}")
        st.write(f"Confianza: {confidence:.2%}")
        if prediction != "no_defecto":
            st.warning("📢 Alerta: posible defecto detectado")
