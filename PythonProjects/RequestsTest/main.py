import requests 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8699c6be05b54dc6d364f2673df948a3'
HEADER = {'Content-Type':'application/json','trainer_token': TOKEN}

pokemons_creation = {
    "name": "Бульбазавр",
    "photo_id": 1
}


changing_pokemon = {
    "pokemon_id": "172223",
    "name": "Andrik",
    "photo_id": 2
}

catch_at_pokeball ={ "pokemon_id": "172223"}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = pokemons_creation,)
print(response.text)'''


'''response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = changing_pokemon ,)
print(response.text)'''


response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = catch_at_pokeball ,)
print(response.text)

