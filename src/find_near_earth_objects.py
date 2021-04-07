import json
from typing import Optional

import requests

from src.models.near_earth_object import FeedAPIObject, NearEarthObject


def main():
    near_earth_objects: FeedAPIObject = get_near_earth_objects_for_url()
    nearest = identify_nearest_dangerous_object(near_earth_objects)
    text = "The closest dangerous approach this week is: {}\nIt has a diameter of {} meters\nIt will fly past ".format(
        nearest.id, nearest.estimated_diameter.meters)

    for close_approach in nearest.close_approaches:
        text = text + "at a distance of {:.2f} kilometers on {}".format(close_approach.miss_distance.kilometers,
                                                                    close_approach.close_approach_date_full)
    print(text)
    with open("index.html", "w") as file:
        file.write(text)


def get_near_earth_objects_for_url(url='https://api.nasa.gov/neo/rest/v1/feed?api_key=DEMO_KEY'):
    return objectify(jsonify(get_from_api(url)))


def get_from_api(url):
    response = requests.get(url)
    return response.content.decode()


def jsonify(response_content):
    return json.loads(response_content)


def objectify(raw_json):
    return FeedAPIObject(raw_json)


def identify_nearest_dangerous_object(objects: FeedAPIObject) -> Optional[NearEarthObject]:
    days = [daily.day for daily in objects.daily_near_earth_objects]
    print("Finding nearest dangerous object for {}".format(days))
    closest_dangerous_neo_distance = float("inf")
    closest_neo = None
    for daily in objects.daily_near_earth_objects:
        for neo in daily.near_earth_objects:
            if neo.is_potentially_hazardous_asteroid:
                for close_approach in neo.close_approaches:
                    if close_approach.miss_distance.kilometers < closest_dangerous_neo_distance:
                        closest_dangerous_neo_distance = close_approach.miss_distance.kilometers
                        closest_neo: NearEarthObject = neo
    return closest_neo


if __name__ == "__main__":
    main()
