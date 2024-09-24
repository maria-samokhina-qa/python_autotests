import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'cfb8ffc3e45d2a3b7841bf6f86e3a1b5'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "Кукумбер",
    "photo_id": 96
}

body_change = {
    "pokemon_id": "74534",
    "name": "Краказявр",
    "photo_id": 15
}

body_pokeball = {
    "pokemon_id": "74534"
}

response_create = requests.post(url=f'{URL}/v2/pokemons', headers=HEADER, json=body_create)
print(response_create.text)

response_change = requests.put(url=f'{URL}/v2/pokemons', headers=HEADER, json=body_change)
print(response_change.text)

response_add_pokeball = requests.post(url=f'{URL}/v2/trainers/add_pokeball', headers=HEADER, json=body_pokeball)
print(response_add_pokeball.text)


