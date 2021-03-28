import json

import requests

r = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
fileURL = json.JSONDecoder().decode(r.content.decode())['hdurl']
r2 = requests.get(fileURL)
with open("test-nasa.jpeg", "wb") as file:
    file.write(r2.content)
