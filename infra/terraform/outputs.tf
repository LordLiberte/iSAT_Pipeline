output "resource_group_name" {
  description = "El nombre del Grupo de Recursos en Azure"
  value       = azurerm_resource_group.rg.name
}

output "acr_name" {
  description = "El nombre de tu Azure Container Registry (necesario para GitHub)"
  value       = azurerm_container_registry.acr.name
}

output "acr_login_server" {
  description = "La URL del servidor de tu registro"
  value       = azurerm_container_registry.acr.login_server
}