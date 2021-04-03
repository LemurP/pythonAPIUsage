from typing import List


class FeedAPIObject:
    def __init__(self, raw_json):
        self.links = Links(raw_json['links'])
        self.element_count: int = raw_json['element_count']
        self.daily_near_earth_objects: List[Daily] = [Daily(day, daily_raw_json) for day, daily_raw_json in
                                                      raw_json['near_earth_objects'].items()]


class Links:
    def __init__(self, raw_json):
        try:
            self.next = raw_json['next']
            self.prev = raw_json['prev']
        except KeyError:
            self.next = ""
            self.prev = ""
        self.self = raw_json['self']


class Daily:
    def __init__(self, day, raw_json):
        self.day: str = day
        self.near_earth_objects: List[NearEarthObject] = [NearEarthObject(raw_json_neo) for raw_json_neo in raw_json]


class NearEarthObject:
    def __init__(self, raw_json):
        self.links = Links(raw_json['links'])
        self.id = raw_json['id']
        self.neo_reference_id = raw_json['neo_reference_id']
        self.name = raw_json['name']
        self.nasa_jpl_url = raw_json['nasa_jpl_url']
        self.absolute_magnitude_h = raw_json['absolute_magnitude_h']
        self.estimated_diameter: EstimatedDiameter = EstimatedDiameter(raw_json['estimated_diameter'])
        self.is_potentially_hazardous_asteroid = raw_json['is_potentially_hazardous_asteroid']
        self.close_approaches: List[CloseApproachData] = [CloseApproachData(raw_json_close_approach) for
                                                          raw_json_close_approach in
                                                          raw_json['close_approach_data']]
        self.is_sentry_object = raw_json['is_sentry_object']

    def get_id(self):
        return self.id


class EstimatedDiameter:
    def __init__(self, raw_json):
        self.kilometers = raw_json['kilometers']
        self.meters = raw_json['meters']
        self.miles = raw_json['miles']
        self.feet = raw_json['feet']


class CloseApproachData:
    def __init__(self, raw_json):
        self.close_approach_date = raw_json['close_approach_date']
        self.close_approach_date_full = raw_json['close_approach_date_full']
        self.epoch_date_close_approach = raw_json['epoch_date_close_approach']
        self.relative_velocity: RelativeVelocity = RelativeVelocity(raw_json['relative_velocity'])
        self.miss_distance: MissDistance = MissDistance(raw_json['miss_distance'])
        self.orbiting_body = raw_json['orbiting_body']


class RelativeVelocity:
    def __init__(self, raw_json):
        self.kilometers_per_second = raw_json['kilometers_per_second']
        self.kilometers_per_hour = raw_json['kilometers_per_hour']
        self.miles_per_hour = raw_json['miles_per_hour']


class MissDistance:
    def __init__(self, raw_json):
        self.astronomical = raw_json['astronomical']
        self.lunar = raw_json['lunar']
        self.kilometers: float = float(raw_json['kilometers'])
        self.miles = raw_json['miles']
