import pandas as pd
import joblib
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier

# 1. Configuración de rutas (usamos Pathlib para que funcione en Windows y Linux/Azure)
BASE_DIR = Path(__file__).parent
RAW_PATH = BASE_DIR / "data" / "raw" / "data.csv"
PROCESSED_PATH = BASE_DIR / "data" / "processed.csv"
MODEL_PATH = BASE_DIR / "models" / "isat_detector.joblib"

def run_pipeline():
    print("🚀 Iniciando Pipeline: ETL + Entrenamiento...")
    
    # --- PASO 1: ETL (Procesamiento de datos) ---
    if not RAW_PATH.exists():
        print(f"❌ Error: No encuentro el archivo {RAW_PATH}")
        print("Asegúrate de haber ejecutado primero: python -m generator.generate")
        return
    
    print(f"Reading data from: {RAW_PATH}")
    df = pd.read_csv(RAW_PATH)
    
    # Aseguramos que la carpeta de destino existe
    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    # Guardamos el archivo procesado que el Dashboard necesita para las gráficas
    df.to_csv(PROCESSED_PATH, index=False)
    print(f"✅ ETL completado: Datos guardados en {PROCESSED_PATH}")

    # --- PASO 2: Entrenamiento del Modelo de IA ---
    print("🧠 Entrenando modelo RandomForest para detección de defectos...")
    
    # Seleccionamos las columnas de entrada (features)
    features = ["tool_wear", "process_pressure", "temperature", "speed"]
    X = df[features]
    y = df["defect"] # Lo que queremos predecir
    
    # Creamos y entrenamos el modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    # Guardamos el modelo en la carpeta /models
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"✅ Modelo entrenado y guardado en {MODEL_PATH}")
    print("\n¡Todo listo! Ahora ya puedes hacer el git push.")

if __name__ == "__main__":
    run_pipeline()