import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'a18760ca11440158d1711d2b51caaebf'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}
TRENER_ID = '2177'

def test_status_code():
    response = requests.get(url= f'{URL}/trainers', params={'trainer_id': TRENER_ID})
    assert response.status_code == 200

def test_name_trener_my():
    response_get = requests.get(url= f'{URL}/trainers', params={'trainer_id': TRENER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Клён'