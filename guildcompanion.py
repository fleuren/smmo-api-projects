import os
import requests

clear = lambda: os.system('cls')
clear()

print("Please input your API key, which can be found in https://web.simple-mmo.com/p-api/home")
api_input = input()
api_key = api_input
clear()

build = "Fleuren's Seasonal Guild Leaderboard App b290425"
notice = f"Note: You may risk suspension of your API token, if you navigate this program too fast.\nCurrent rules for API use is 40 calls per minute. This program currently uses 4 calls per instance.\n\nThere is no implementation of a 'live' counter as of this build, please tread carefully."
number_formatting = "{:,}"

print(notice)

#LEADERBOARD
def sgl():
    currentseason_endpoint = f'https://api.simple-mmo.com/v1/guilds/seasons?api_key={api_key}'
    currentseason_response = requests.post(currentseason_endpoint)
    for i in range(500):
            try:
                season_id = currentseason_response.json()[i]['id']
            except:
                continue
    print(build)
    print(f"Printing details for Season {season_id}\n")
    seasonLB_endpoint = f'https://api.simple-mmo.com/v1/guilds/seasons/{season_id}?api_key={api_key}'
    seasonLB_response = requests.post(seasonLB_endpoint)

    for i in range(50):
        sgl_pos = seasonLB_response.json()[i]['position']
        sgl_id = seasonLB_response.json()[i]['guild']['id']
        sgl_name = seasonLB_response.json()[i]['guild']['name']
        sgl_exp = seasonLB_response.json()[i]['experience']
        sgl_exp_readable = number_formatting.format(sgl_exp)

        print(f"•\t{sgl_pos} | {sgl_id} | {sgl_name}\n\tExperience: {sgl_exp_readable}\n")
    print(f"\nWhere would you like to go?\n1. Leaderboard\n2. Check a specific guild:")
    command = int(input())
    menu(command)
def guild_specific(gs_id):
                gs_warrior = 0
                gs_safe = 0
                clear()
                print(build)
                print(f"Printing the details for Guild ID: {gs_id}\n")
                gs_endpoint = f'https://api.simple-mmo.com/v1/guilds/info/{gs_id}?api_key={api_key}'
                gs_response = requests.post(gs_endpoint)
                gsx_endpoint = f'https://api.simple-mmo.com/v1/guilds/members/{gs_id}?api_key={api_key}'
                gsx_response = requests.post(gsx_endpoint)
                gs_name = gs_response.json()['name']
                gs_membercount = gs_response.json()['member_count']
                gs_ownerid = gs_response.json()['owner']
                gs_exp = gs_response.json()['current_season_exp']
                gs_exp_readable = number_formatting.format(gs_exp)
                gs_war = gs_response.json()['eligible_for_guild_war']
                
                for i in range (gs_membercount):
                    member_warrior = gsx_response.json()[i]['warrior']
                    member_safe = gsx_response.json()[i]['safe_mode']
                    if member_warrior == 1:
                        gs_warrior += 1
                    if member_safe == 1:
                        gs_safe += 1
                
                ownerid_endpoint = f'https://api.simple-mmo.com/v1/player/info/{gs_ownerid}?api_key={api_key}'
                ownerid_response = requests.post(ownerid_endpoint)
                
                gs_owner = ownerid_response.json()['name']
                print(f'Name\t | {gs_name}\nLeader\t | {gs_owner}\n\nMember/s:  {gs_membercount} | Warriors: {gs_warrior} | In safe mode: {gs_safe}\nCan participate in war: {gs_war}\n\nExp | {gs_exp_readable}')
                print(f'\nExtra info (in-game guild webpage):\nhttps://web.simple-mmo.com/guilds/view/{gs_id}?new_page=true\n')
                print(f'Guild Members:\nSafe Mode: 🔷/🔶 | Warrior: ⚔️/🌱\n')
                for i in range (gs_membercount):
                    member_id = gsx_response.json()[i]['user_id']
                    member_name = gsx_response.json()[i]['name']
                    member_level = gsx_response.json()[i]['level']
                    level_readable = number_formatting.format(member_level)
                    member_role = gsx_response.json()[i]['position']
                    member_safe = gsx_response.json()[i]['safe_mode']
                    member_warrior = gsx_response.json()[i]['warrior']
                    safe_readable = str
                    warrior_readable = str
                    if member_safe == 1:
                        safe_readable = "🔷"
                    else:
                        safe_readable = "🔶"
                    
                    if member_warrior == 1:
                        warrior_readable = "🔪"
                    else:
                        warrior_readable = "🌱"
                    
                    print(f"Name: {member_name} | {warrior_readable}{safe_readable} | {member_id}\nLevel: {level_readable} | Position: {member_role}\n")
                print(f"\n{notice}\n")
                
                print(f"Where would you like to go?\n1. Leaderboard\n2. Check a specific guild:")
                command = int(input())
                menu(command)

def menu(command):
    clear()
    if command == 1:
        sgl()
    if command == 2:
        clear()
        print(f"Input the ID of the guild you'd like to take a further look into, or input 0 to quit.")
        guild_id = int(input())
        guild_specific(guild_id)
    if command == 0:
        print("Program closed.")
print(f"Where would you like to go?\n1. Leaderboard\n2. Check a specific guild:")
command = int(input())
menu(command)
