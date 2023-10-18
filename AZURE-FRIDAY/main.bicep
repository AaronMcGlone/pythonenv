param location string = resourceGroup().location

module mystorageDeploy 'storage.bicep' = {
  name: 'mystorageDeploy'
  params: {
    namePrefix: 'alfan'
    location: location 
  }
}

output blobUri string = mystorageDeploy.outputs.blobUri
