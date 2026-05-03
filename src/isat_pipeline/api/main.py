from fastapi import FastAPI
from .routers import health, piezas, alertas

app = FastAPI(
    title="iSAT Pipeline API",
    description="API para el pipeline de detección de piezas defectuosas",
    version="0.1.0",
)

app.include_router(health.router)
app.include_router(piezas.router, prefix="/piezas", tags=["piezas"])
app.include_router(alertas.router, prefix="/alertas", tags=["alertas"])
