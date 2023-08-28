import json
import os.path
import pytest
from fixture.application import Application


fixture = None

@pytest.fixture(scope='session')
def app():
    global fixture
    fixture = Application()
    return fixture

@pytest.fixture()
def credentials():
    credentials_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "credentials.json")
    with open(credentials_file) as file:
        credentials_json = json.load(file)
    return credentials_json

@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def finalizer():
        fixture.destroy()

    request.addfinalizer(finalizer)
    return fixture
