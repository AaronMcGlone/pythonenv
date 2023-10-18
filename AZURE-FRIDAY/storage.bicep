param namePrefix string
param location string = resourceGroup().location

resource mystorage 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: '${namePrefix}${uniqueString(resourceGroup().id)}'
  location: location 
  kind: 'StorageV2'
  sku: {
    name:'Premium_LRS'
  }
}

output blobUri string = mystorage.properties.primaryEndpoints.blob 
