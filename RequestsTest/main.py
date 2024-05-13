import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'a18760ca11440158d1711d2b51caaebf'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}

body_sozdanie_p = {
    "name": "zavrik",
    "photo": "https://dolnikov.ru/pokemons/albums/007.png"
}

body_name_mena = {
    "pokemon_id": "27173",
    "name": "klop"
}
body_pokeball ={
    "pokemon_id": "27173"
}

response=requests.post(url= f'{URL}/pokemons', headers= HEADER, json= body_sozdanie_p)
print(response.text)

response=requests.patch(url= f'{URL}/pokemons', headers= HEADER, json= body_name_mena)
print(response.text)

response=requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADER, json= body_pokeball)
print(response.text)