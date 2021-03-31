import json

import requests


def getFromAPIAndJsonify(url):
    response = requests.get(url)
    json_decoder = json.JSONDecoder()
    response_content = response.content.decode()
    return json_decoder.decode(response_content)


if __name__ == "__main__":
    near_earth_objects = getFromAPIAndJsonify('https://api.nasa.gov/neo/rest/v1/feed?api_key=DEMO_KEY')
    only_dangerous = near_earth_objects['near_earth_objects']
