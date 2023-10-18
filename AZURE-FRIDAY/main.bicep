param location string = resourceGroup().location
param namePrefix string
param ipRules array

module mystorageDeploy 'storage.bicep' = {
  name: 'mystorageDeploy'
  params: {
    namePrefix: namePrefix
    location: location 
    ipRules: ipRules
  
  }
}

output blobUri string = mystorageDeploy.outputs.blobUri
