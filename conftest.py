import pytest
import requests
from helpers import *
from data import Urls

@pytest.fixture
def create_new_user_and_delete():
    payload_cred = random_payload()
    response = requests.post(f"{Urls.BASE_URL}{Urls.USER_CREATE_URL}", data=payload_cred)
    yield payload_cred, response
    access_token = response.json()['accessToken']
    requests.delete(f"{Urls.BASE_URL}{Urls.USER_DATA_UPDATE_URL}", headers={'Authorization': access_token})