import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--runrealcalls", action="store_true", default=False, help="run real calls to the apis in tests"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "calls_real_api: mark test as calling real apis")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runrealcalls"):
        # do not skip real api calls tests
        return
    skip_real_calls = pytest.mark.skip(reason="need --runrealcalls option to run")
    for item in items:
        if "calls_real_api" in item.keywords:
            item.add_marker(skip_real_calls)
