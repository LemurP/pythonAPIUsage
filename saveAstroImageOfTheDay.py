import json

import requests

response = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
json_decoder = json.JSONDecoder()
response_content = response.content.decode()
json_representation = json_decoder.decode(response_content)
fileURL = json_representation['hdurl']
r2 = requests.get(fileURL)

with open("test-nasa.jpeg", "wb") as file:
    file.write(r2.content)
