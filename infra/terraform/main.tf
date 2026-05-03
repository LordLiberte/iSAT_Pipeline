terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "isat_data" {
  bucket = "isat-pipeline-data-${random_pet.bucket_suffix.id}"
  acl    = "private"

  versioning {
    enabled = true
  }
}

resource "aws_ecr_repository" "isat_repository" {
  name = "isat-pipeline"
}

resource "random_pet" "bucket_suffix" {
  length = 2
}
