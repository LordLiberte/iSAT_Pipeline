# Infraestructura con Terraform

Este directorio contiene un ejemplo de infraestructura para AWS.

## Requisitos
- Cuenta AWS con credenciales configuradas.
- Terraform 1.5 o superior.

## Pasos para desplegar
1. Configura tus credenciales AWS:
   - `aws configure`
2. Inicializa Terraform:
   - `cd infra/terraform`
   - `terraform init`
3. Revisa el plan:
   - `terraform plan`
4. Aplica la infraestructura:
   - `terraform apply`
   - Confirma con `yes`.

## Recursos creados
- Bucket S3 privado para datos.
- Repositorio ECR para imágenes Docker.

## Uso posterior
- Usa la URL de salida `ecr_repository_url` para subir imágenes Docker.
- Usa el bucket S3 para almacenar datos ETL y resultados.
