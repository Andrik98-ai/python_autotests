
import requests 
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8699c6be05b54dc6d364f2673df948a3'
HEADER = {'Content-Type':'application/json','trainer_token': TOKEN}
TRAINER_ID = '12636'
def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200


def test_trainers_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Andrik'


   
