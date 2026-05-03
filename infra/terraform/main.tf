terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# 1. Grupo de Recursos en Madrid
resource "azurerm_resource_group" "rg" {
  name     = "isat-pipeline-rg"
  location = "Spain Central" 
}

# 2. Número aleatorio
resource "random_integer" "ri" {
  min = 10000
  max = 99999
}

# 3. Almacén de Contenedores (ACR) con nombre nuevo
resource "azurerm_container_registry" "acr" {
  name                = "isatreg${random_integer.ri.result}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = true
}