# iSAT_Pipeline

Pipeline DataOps para detectar piezas defectuosas con ETL, ML, API y dashboard.

## Tecnologías principales
- Python 3.11
- FastAPI + Pydantic v2
- SQLite / SQLModel
- scikit-learn + joblib
- Streamlit
- Docker + Docker Compose
- GitHub Actions
- Prefect para orquestación
- Terraform para IaC en AWS

## Estructura del repositorio
- `src/isat_pipeline/`: código principal del pipeline.
- `dashboard/app.py`: dashboard de Streamlit.
- `generator/generate.py`: datos sintéticos para pruebas.
- `data/`: datos generados y procesados.
- `models/`: modelos guardados.
- `tests/`: pruebas unitarias.
- `AuxiliarMDs/`: documentación de metodología ágil.
- `.github/workflows/ci.yml`: CI con tests y build Docker.
- `infra/terraform/`: infraestructura de ejemplo para AWS.

## Inicio rápido
1. Instala dependencias:
   - `pip install -r requirements.txt`
2. Genera datos sintéticos:
   - `make generate`
3. Ejecuta el pipeline ETL/ML:
   - `make flow`
4. Inicia la API:
   - `make run-api`
5. Inicia el dashboard:
   - `make run-dashboard`

## Docker
- Construir imagen: `make docker-build`
- Levantar servicios: `make compose-up`

## GitHub Actions
El workflow `.github/workflows/ci.yml` ejecuta:
- instalación de dependencias
- tests y cobertura
- lint con ruff
- build de Docker

## Infraestructura AWS
Consulta `infra/terraform/README.md` para los pasos de despliegue.

## Metodología ágil
- `AuxiliarMDs/PRODUCT_BACKLOG.md`
- `AuxiliarMDs/SPRINTS.md`
- `AuxiliarMDs/RETROSPECTIVE.md`
- `AuxiliarMDs/MEMORIA_PROYECTO.md`
