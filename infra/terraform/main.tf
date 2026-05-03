terraform {
  required_version = ">= 1.5.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0" # Usamos una versión estable de Azure
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {} # Este bloque es obligatorio para Azure
}

variable "azure_region" {
  default     = "East US"
  description = "Región de Azure donde se desplegará la infraestructura"
}

# 1. GRUPO DE RECURSOS (Obligatorio en Azure)
resource "azurerm_resource_group" "isat_rg" {
  name     = "isat-pipeline-rg"
  location = var.azure_region
}

# Generador de sufijo aleatorio (sin guiones ni mayúsculas para cumplir con las reglas de Azure)
resource "random_string" "suffix" {
  length  = 6
  special = false
  upper   = false
}

# 2. EQUIVALENTE A AWS S3 BUCKET (Storage Account + Container)
resource "azurerm_storage_account" "isat_storage" {
  name                     = "isatdata${random_string.suffix.result}" # Nombre único global
  resource_group_name      = azurerm_resource_group.isat_rg.name
  location                 = azurerm_resource_group.isat_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS" # Replicación local (más barata)
}

resource "azurerm_storage_container" "isat_container" {
  name                  = "isat-pipeline-data"
  storage_account_name  = azurerm_storage_account.isat_storage.name
  container_access_type = "private"
}

# 3. EQUIVALENTE A AWS ECR (Azure Container Registry)
resource "azurerm_container_registry" "isat_acr" {
  name                = "isatpipelineacr${random_string.suffix.result}" # Nombre único global
  resource_group_name = azurerm_resource_group.isat_rg.name
  location            = azurerm_resource_group.isat_rg.location
  sku                 = "Basic" # La capa más económica
  admin_enabled       = true  # Nos permitirá hacer "docker login" fácilmente
}