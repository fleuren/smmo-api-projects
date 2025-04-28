import requests
import os
clear = lambda: os.system('cls')
clear()
print("Please input your API key. You can find this at: https://web.simple-mmo.com/p-api/home")
api_key = input()
host_endpoint = f'https://api.simple-mmo.com/v1/player/me?api_key={api_key}'
host_response = requests.post(host_endpoint)

clear()
guild_ID = host_response.json()['guild']['id']
guild_NAME = host_response.json()['guild']['name']
print(f"{guild_ID} | {guild_NAME}\n")

tournament_endpoint = f'https://api.simple-mmo.com/v1/guilds/members/{guild_ID}?api_key={api_key}'
tournament_response = requests.post(tournament_endpoint)
def level():
    for i in range(80):
        try:
            member_name = tournament_response.json()[i]['name']
            member_id = tournament_response.json()[i]['user_id']
            member_level = tournament_response.json()[i]['level']
            print(f"ID: {member_id} |Username: {member_name}\nLevel: {member_level}")
        except:
            continue
    print(f"Member Count: {i}")


level()
rateLimit = host_response.headers["X-RateLimit-Remaining"]
