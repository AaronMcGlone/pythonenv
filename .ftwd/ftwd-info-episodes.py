# Import modules that this script/function needs to use
import requests, json

# The API URL that we'll be requesting from
url = "https://api.tvmaze.com/shows/1824/"
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

for item in json_response:
    print(f'{item["number"]}: {item["name"]} (season: {item["season"]}, airdate: {item["airdate"]})')
    