$resources = @(
    'module.synapse_sql_server[0].azurerm_synapse_managed_private_endpoint.data_lake',
    'module.synapse_workspace_private.azurerm_synapse_managed_private_endpoint.data_lake',
    'module.synapse_workspace_private.azurerm_synapse_managed_private_endpoint.data_lake_failover',
    'module.synapse_workspace_private.azurerm_synapse_managed_private_endpoint.synapse_mpe_kv',
    'module.synapse_workspace_private.azurerm_synapse_role_assignment.synapse["Synapse Compute Operator.a66ee73a-c31b-451d-b13e-19b4e92c0c25"]',
    'module.synapse_workspace_private.azurerm_synapse_role_assignment.synapse["Synapse Contributor.0a5073e3-b8e9-4786-8e1f-39f2c277aeb2"]',
    'module.synapse_workspace_private.azurerm_synapse_role_assignment.synapse["Synapse Administrator.6a38f212-3834-4e2e-93fb-f81bb3a3fe49"]',
    'module.synapse_workspace_private.azurerm_synapse_role_assignment.synapse["Synapse Administrator.875e931a-ee45-425e-acde-1ec24a8a290d"]'
)

foreach ($resource in $resources) {
    terraform state rm $resource
}
