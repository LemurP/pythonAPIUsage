import requests
from PIL import Image
import json
r = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
fileURL = json.JSONDecoder().decode(r.content.decode())['hdurl']
r2 = requests.get(fileURL)
f = open("test-nasa.jpeg","wb")
f.write(r2.content)
f.close()

