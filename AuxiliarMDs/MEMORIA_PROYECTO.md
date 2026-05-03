# Memoria del Proyecto iSAT_Pipeline

## Resumen ejecutivo
El proyecto iSAT_Pipeline construye un pipeline DataOps para identificar piezas defectuosas en una línea prioritaria de producción. Usa Python, FastAPI, Streamlit y scikit-learn para automatizar ETL, entrenamiento y detección en tiempo real.

## Arquitectura
- Fuente de datos: CSV sintético generado por `generator/generate.py`.
- Capa ETL: `src/isat_pipeline/parsing/protocolo_isat.py` limpia y transforma datos.
- Modelo ML: `src/isat_pipeline/ml/detector.py` entrena un clasificador RandomForest.
- API backend: `src/isat_pipeline/api/main.py` expone endpoints de salud y predicción.
- Dashboard: `dashboard/app.py` muestra métricas y permite predicción de piezas.
- Orquestación: `src/isat_pipeline/orchestrator.py` con Prefect para ejecutar el pipeline.

## Decisiones técnicas
- Python 3.11 para compatibilidad con el stack académico.
- SQLite por simplicidad y portabilidad.
- Streamlit para un dashboard rápido sin frontend adicional.
- Docker y Docker Compose para entornos reproducibles.
- GitHub Actions para asegurar la calidad y build continua.

## Metodología ágil empleada
- Se usó enfoque SCRUM/Kanban híbrido.
- El backlog está documentado en `AuxiliarMDs/PRODUCT_BACKLOG.md`.
- Se registraron al menos 3 sprints en `AuxiliarMDs/SPRINTS.md`.
- Se completó una retrospectiva en `AuxiliarMDs/RETROSPECTIVE.md`.

## Conclusiones
- La automatización básica del pipeline funciona localmente.
- El proyecto es viable como demostración de DataOps y CI/CD.
- Como siguiente paso, se recomienda conectar el pipeline a datos reales y desplegar en AWS con Terraform.
