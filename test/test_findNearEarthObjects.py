import pytest

from findNearEarthObjects import getFromAPIAndJsonify


@pytest.mark.calls_real_api
def test_known_result_from_neo_api_call():
    near_earth_objects = getFromAPIAndJsonify(
        'https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-01-01&end_date=2021-01-01&api_key=DEMO_KEY')
    with open("test/test_neo_call_response.json", "r") as file:
        contents = file.read()
        assert str(near_earth_objects) == contents
