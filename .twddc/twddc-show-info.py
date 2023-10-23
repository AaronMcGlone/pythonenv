# the walking dead

import requests

url = "https://api.tvmaze.com/shows/60879"

querystring = {"q":"'walking dead'"}

payload = ""
headers = {
    "Accept": "application/json"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(f'{response} {url}')
print(response.text)