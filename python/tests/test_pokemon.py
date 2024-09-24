import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'cfb8ffc3e45d2a3b7841bf6f86e3a1b5'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
trainer_id = '5454'

def test_status_code():
    response = requests.get(url = f'{URL}/v2/pokemons', params = {'trainer_id': trainer_id})
    assert response.status_code == 200

@pytest.mark.parametrize('key, value', [('trainer_id', trainer_id)])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/v2/pokemons', params = {'trainer_id': trainer_id})
    assert response_parametrize.json()["data"][0][key] == value

