# Sprint Retrospective

## Qué funcionó
- El pipeline ETL quedó documentado y automatizado con Prefect.
- El API REST y el dashboard se desarrollaron con el stack previsto.
- Se creó un workflow de CI/CD en GitHub Actions.

## Qué no funcionó o quedó por mejorar
- La orquestación con Prefect todavía requiere un despliegue de servidor.
- La integración de IaC con AWS se dejó en un esqueleto porque no hay cuenta activa configurada.
- Faltan métricas de producción reales y datos de línea de fábrica.

## Próximos pasos
- Añadir un scheduler en Prefect y conectar al Cloud de Prefect.
- Completar el despliegue AWS con Terraform y ECR/ECS.
- Incrementar el dataset real para mejorar la validación del modelo.
