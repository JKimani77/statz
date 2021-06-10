import requests
import urllib.request, json
from .models import *



url = "https://free-football-soccer-videos.p.rapidapi.com/"

headers = {
    'x-rapidapi-key': "6c61f61a64mshb7f6dd3b49823b4p1ea082jsnbd55b4b7071b",
    'x-rapidapi-host': "free-football-soccer-videos.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

#
# print(response.text)