import os
import requests

clear = lambda: os.system('cls')
clear()

print("Please input your API key, which can be found in https://web.simple-mmo.com/p-api/home")
api_key = input()
clear()

print(f"Which season would you like to track?")
season_ID = int(input())
clear()

print(f"Printing details for Season {season_ID}\n")
seasonLB_endpoint = f'https://api.simple-mmo.com/v1/guilds/seasons/{season_ID}?api_key={api_key}'
seasonLB_response = requests.post(seasonLB_endpoint)

for i in range(50):
    sgl_pos = seasonLB_response.json()[i]['position']
    sgl_id = seasonLB_response.json()[i]['guild']['id']
    sgl_name = seasonLB_response.json()[i]['guild']['name']
    sgl_exp = seasonLB_response.json()[i]['experience']

    print(f"•\t{sgl_pos} | {sgl_id} | \t{sgl_name}\n\tExperience: {sgl_exp}\n")

def guild_specific(gs_id):
    while gs_id != 0:
            clear()
            print(f"Printing the details for Guild ID: {gs_id}\n")
            gs_endpoint = f'https://api.simple-mmo.com/v1/guilds/info/{gs_id}?api_key={api_key}'
            gs_response = requests.post(gs_endpoint)

            gs_name = gs_response.json()['name']
            gs_membercount = gs_response.json()['member_count']
            gs_ownerid = gs_response.json()['owner']
            gs_exp = gs_response.json()['current_season_exp']
            
            ownerid_endpoint = f'https://api.simple-mmo.com/v1/player/info/{gs_ownerid}?api_key={api_key}'
            ownerid_response = requests.post(ownerid_endpoint)
            
            gs_owner = ownerid_response.json()['name']
            print(f'ID\t | {gs_id}\nName\t | {gs_name}\nMember/s | {gs_membercount}\nLeader\t | {gs_owner}\nExp\t | {gs_exp}')
            print(f"Input the ID of the guild you'd like to take a further look into:")
            gs_id = int(input())

print(f"Input the ID of the guild you'd like to take a further look into:")
guild_id = int(input())
guild_specific(guild_id)
