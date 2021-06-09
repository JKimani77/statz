from django.shortcuts import render

# Create your views here.
import http.client

conn = http.client.HTTPSConnection("free-football-soccer-videos.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "6c61f61a64mshb7f6dd3b49823b4p1ea082jsnbd55b4b7071b",
    'x-rapidapi-host': "free-football-soccer-videos.p.rapidapi.com"
    }

conn.request("GET", "/", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
