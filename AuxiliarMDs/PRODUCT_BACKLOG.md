# Product Backlog

## Objetivo general
Construir un pipeline DataOps completo para analizar datos de producción y detectar piezas defectuosas en tiempo real.

## Historias de usuario

1. Como operario, quiero visualizar el estado del proceso y la tasa de defectos para priorizar acciones de mantenimiento.
2. Como analista, quiero un pipeline ETL que cargue datos crudos, los procese y los prepare para entrenamiento automático.
3. Como ingeniero, quiero un modelo de ML entrenado que clasifique defectos en la producción.
4. Como responsable, quiero un API REST para recibir observaciones en tiempo real y devolver alertas.
5. Como gestor, quiero que el proyecto se ejecute con Docker y tenga CI/CD con GitHub Actions.
6. Como equipo, quiero documentación de arquitectura, decisión técnica y metodología ágil para la entrega.

## Priorización
- Alta: ETL, modelo ML, API, documentación, pruebas.
- Media: dashboard de visualización, IaC en Terraform, presentación.

## Criterios de aceptación
- El repositorio funciona en local con Docker.
- El pipeline ETL se automatiza con Prefect.
- El modelo puede predecir defectos con datos sintéticos.
- Hay tests automáticos y un workflow CI en GitHub Actions.
