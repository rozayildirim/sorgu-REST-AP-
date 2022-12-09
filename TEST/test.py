import requests

URL = "https://coffee.alexflipnote.dev/random.json"

result =  requests.get(URL)

data = result.json()
print(data)