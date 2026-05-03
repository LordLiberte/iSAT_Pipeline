output "s3_bucket_name" {
  description = "Nombre del bucket S3 para datos procesados"
  value       = aws_s3_bucket.isat_data.id
}

output "ecr_repository_url" {
  description = "URL del repositorio ECR para las imágenes Docker"
  value       = aws_ecr_repository.isat_repository.repository_url
}
