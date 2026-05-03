# Arquitectura del proyecto iSAT_Pipeline

## Componentes
- `generator/generate.py`: Genera datos sintéticos de producción con posibles defectos.
- `src/isat_pipeline/parsing/protocolo_isat.py`: ETL para cargar, limpiar y transformar datos.
- `src/isat_pipeline/ml/detector.py`: Entrena y guarda un modelo de detección de defectos.
- `src/isat_pipeline/api/main.py`: API REST con FastAPI para predicciones y salud.
- `dashboard/app.py`: Dashboard de Streamlit para métricas y pruebas de inferencia.
- `src/isat_pipeline/orchestrator.py`: Flujo de Prefect que ejecuta ETL, procesamiento y entrenamiento.

## Flujo de datos
1. Generación de datos sintéticos en `data/raw/data.csv`.
2. Carga y limpieza en `load_raw_data` y `clean_data`.
3. Guardado de datos procesados en `data/processed/processed.csv`.
4. Entrenamiento del modelo y guardado en `models/isat_detector.joblib`.
5. Consulta del modelo desde la API REST y desde el dashboard.

## Decisiones de diseño
- SQLite y archivos planos para mantener el proyecto reproducible sin infraestructura compleja.
- Prefect para separar la lógica de orquestación de la implementación de negocio.
- Docker para encapsular el entorno y permitir despliegue local o en nube.

## Diagrama conceptual
- Fuente -> ETL -> Almacenamiento procesado -> Modelo ML -> API y Dashboard
