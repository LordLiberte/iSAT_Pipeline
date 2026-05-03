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

# 1. Crear el Grupo de Recursos en Azure
resource "azurerm_resource_group" "rg" {
  name     = "isat-pipeline-rg"
  location = "West Europe" # Puedes cambiarlo por "East US" u otra región si prefieres
}

# 2. Crear un número aleatorio para que el nombre del ACR sea único mundialmente
resource "random_integer" "ri" {
  min = 10000
  max = 99999
}

# 3. Crear el Almacén de Contenedores (ACR)
resource "azurerm_container_registry" "acr" {
  name                = "isatregistry${random_integer.ri.result}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = true
}