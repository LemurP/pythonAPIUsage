import json

import requests


def getFromAPI(url):
    response = requests.get(url)
    return response.content.decode()


def jsonify(response_content):
    return json.loads(response_content)


if __name__ == "__main__":
    near_earth_objects = jsonify(getFromAPI('https://api.nasa.gov/neo/rest/v1/feed?api_key=DEMO_KEY'))
    only_dangerous = near_earth_objects['near_earth_objects']


def identify_nearest_dangerous_object(input_json):
    days: dict = input_json['near_earth_objects']
    result = None
    result_distance = float("inf")
    for neos in days.values():
        for neo in neos:
            if neo['is_potentially_hazardous_asteroid']:
                if result_distance > float(neo['close_approach_data'][0]['miss_distance']['kilometers']):
                    result = neo
                    result_distance = float(neo['close_approach_data'][0]['miss_distance']['kilometers'])

    return result
