import pytest

from src.find_near_earth_objects import getFromAPI, jsonify, identify_nearest_dangerous_object


@pytest.mark.calls_real_api
def test_known_result_from_neo_api_call():
    near_earth_objects = jsonify(getFromAPI(
        'https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-01-01&end_date=2021-01-01&api_key=DEMO_KEY'))
    with open("test/test_neo_call_response.json", "r") as file:
        contents = file.read()
        assert str(near_earth_objects) == contents


@pytest.mark.calls_real_api
def test_nearest_object_with_dangerous_tag_is_identified():
    near_earth_objects = jsonify(getFromAPI(
        'https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-01-02&end_date=2021-01-02&api_key=DEMO_KEY'))
    result = near_earth_objects

    nearest_dangerous_object = identify_nearest_dangerous_object(result)
    assert nearest_dangerous_object['id'] == '54095182'


# Dummy test so pytest won't fail in pipeline
def dummy_test():
    pass
