# Import modules that this script/function needs to use
import requests, json, os
from azure.data.tables import TableServiceClient

table_name = 'movieepisode'
conn_str = ''
table_service_client = TableServiceClient.from_connection_string(conn_str=conn_str)
table_client = table_service_client.get_table_client(table_name=table_name)

# The API URL that we'll be requesting from
url = "https://api.tvmaze.com/shows/73/"
# Specific resource from the API URL for a/some particular data
resource = 'episodes'
# Build the final host/url to be queried
host = f'{url}{resource}'
# Define any parameters
querystring = {"q":"'walking dead'"}
# Define any 'body' payload (non in this example)
payload = ""
# Headers for the request
headers = {
    "Accept": "application/json"
}

# Create a variable 'response' to contain the response from the API Request
response = requests.get(host, data=payload, headers=headers, params=querystring)
print(f'{response} {host}')

#print(response.text)
# We reviewed data at: https://jsonformatter.curiousconcept.com/

# New variable with the text (data/payload) converted into JSON for processing.
json_response = json.loads(response.text)
print(f'Number of records in array/list (length): {len(json_response)}')

entry_count = 0
for episode in json_response:# (Array/List: for thing in list)
    #print(f'{item["number"]}: {item["name"]} (season: {item["season"]}, airdate: {item["airdate"]})')
    entry_template = {
        u"PartitionKey": "the-walking-dead",
        u"RowKey": str(episode["id"])
    }
    entry = dict(entry_template)
    for i, (k,v) in enumerate(episode.items()):# (Dictionary: for (index) item/s in dict)
        if isinstance(v,str) or isinstance(v,int):
            entry.update({k:v})
        elif k == 'image':
            entry.update({k:v['medium']})
    entry_count = entry_count + 1
    entry = table_client.upsert_entity(entity=entry)
    print(entry_count)
    