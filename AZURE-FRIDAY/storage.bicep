param namePrefix string
param location string = resourceGroup().location
param ipRules array

resource mystorage 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: '${namePrefix}${uniqueString(resourceGroup().id)}'
  location: location 
  kind: 'StorageV2'
  sku: {
    name:'Standard_LRS'
  }
  properties: {
    networkAcls: {
      defaultAction: 'Deny'
      bypass: 'AzureServices'
      ipRules: ipRules
    }
  }
}

output blobUri string = mystorage.properties.primaryEndpoints.blob 
