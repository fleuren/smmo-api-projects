import os
import requests
import time

clear = lambda: os.system('cls')
clear()

print("Please input your API key, which can be found in https://web.simple-mmo.com/p-api/home")
api_input = input()
api_key = api_input
clear()

build = "Fleuren's Seasonal Guild Leaderboard App b300425"
notice = f"Note: You may risk suspension of your API token, if you navigate this program too fast.\nCurrent rules for API use is 40 calls per minute. This program currently uses 4 calls per instance.\n\nThere is no implementation of a 'live' counter as of this build, please tread carefully."
number_formatting = "{:,}"
command_menu =f"Where would you like to go?\n1. Leaderboard (2 API calls)\n2. Check a specific guild (3 API calls)\n3. PVP Simulator (2 API calls)\n4. Guild Difference Calculator (3 API calls)\n\n0. Quit"
warn_menu = "Note that there is no way to go back to the menu as of this build. Press 1 to pass this step."


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
    print(command_menu)
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
                    member_inactive = gsx_response.json()[i]['last_activity']
                    current_time = time.time()
                    days_inactive1 = current_time-member_inactive
                    days_inactive2 = days_inactive1/86400
                    days_inactive_int = int(days_inactive2)
                    days_inactive_readable = str
                    if days_inactive_int == 0:
                        days_inactive_readable = "Active / Active less than a day ago"
                    elif days_inactive_int == 1:
                        days_inactive_readable = f"Inactive for {days_inactive_int} day."
                    else:
                        days_inactive_readable = f"Inactive for {days_inactive_int} days."

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
                    
                    print(f"Name: {member_name} | {warrior_readable}{safe_readable} | {member_id}\nLevel: {level_readable} | Position: {member_role}\nActivity (in days): {days_inactive_readable} \n")
                print(f"\n{notice}\n")
                
                print(command_menu)
                command = int(input())
                menu(command)

def simulation(player_id):
    
    playerinfo_endpoint = f'https://api.simple-mmo.com/v1/player/info/{player_id}?api_key={api_key}'
    playerinfo_response = requests.post(playerinfo_endpoint)
    yourinfo_endpoint = f'https://api.simple-mmo.com/v1/player/me?api_key={api_key}'
    yourinfo_response = requests.post(yourinfo_endpoint)

    player_name = playerinfo_response.json()['name']
    player_level = playerinfo_response.json()['level']
    player_currenthp = playerinfo_response.json()['hp']
    player_maxhp = playerinfo_response.json()['max_hp']
    player_safemode = playerinfo_response.json()['safeMode']
    pchp_readable = number_formatting.format(player_currenthp)
    pmhp_readable = number_formatting.format(player_maxhp)
    psm_readable = str
    if player_safemode == 1:
        psm_readable = "🌱"
    else:
        psm_readable = "🔪"

    player_str = playerinfo_response.json()['str']
    player_str2 = playerinfo_response.json()['bonus_str']
    player_def = playerinfo_response.json()['def']
    player_def2 = playerinfo_response.json()['bonus_def']
    player_dex = playerinfo_response.json()['dex']
    player_dex2 = playerinfo_response.json()['bonus_dex']

    playertotalstr = player_str + player_str2
    playertotaldef = player_def + player_def2
    playertotaldex = player_dex + player_dex2

    ptstr_readable = number_formatting.format(playertotalstr)
    ptdef_readable = number_formatting.format(playertotaldef)
    ptdex_readable = number_formatting.format(playertotaldex)

    your_name = yourinfo_response.json()['name']
    your_level = yourinfo_response.json()['level']
    your_currenthp = yourinfo_response.json()['hp']
    your_maxhp = yourinfo_response.json()['max_hp']
    your_safemode = yourinfo_response.json()['safeMode']
    ychp_readable = number_formatting.format(your_currenthp)
    ymhp_readable = number_formatting.format(your_maxhp)
    ysm_readable = str
    if your_safemode == 1:
        ysm_readable = "🌱"
    else:
        ysm_readable = "🔪"

    your_str = yourinfo_response.json()['str']
    your_str2 = yourinfo_response.json()['bonus_str']
    your_def = yourinfo_response.json()['def']
    your_def2 = yourinfo_response.json()['bonus_def']
    your_dex = yourinfo_response.json()['dex']
    your_dex2 = yourinfo_response.json()['bonus_dex']

    yourtotalstr = your_str + your_str2
    yourtotaldef = your_def + your_def2
    yourtotaldex = your_dex + your_dex2

    ytstr_readable = number_formatting.format(yourtotalstr)
    ytdef_readable = number_formatting.format(yourtotaldef)
    ytdex_readable = number_formatting.format(yourtotaldex)

    print(f"Tracking details of {player_name} | {psm_readable}")
    print(f"Health: {pchp_readable}/{pmhp_readable} | Level: {player_level}\nSTR: {ptstr_readable} | DEF: {ptdef_readable} | DEX: {ptdex_readable}\n")

    print(f"Tracking your details ({your_name}) | {ysm_readable}")
    print(f"Health: {ychp_readable}/{ymhp_readable} | Level: {your_level}\nSTR: {ytstr_readable} | DEF: {ytdef_readable} | DEX: {ytdex_readable}\n")

    playerpoint = 0
    yourpoint = 0

    print(f"Simulation: {player_name} vs. {your_name}")
    if playertotalstr > yourtotaldef:
        print(f" • {player_name}'s STR, is higher than {your_name}'s DEF")
        playerpoint += 1
    else:
        yourpoint += 1
        print(f" • {your_name}'s STR, is higher than {player_name}'s DEF")

    if playertotaldef > yourtotalstr:
        playerpoint += 1
        print(f" • {player_name}'s DEF, is higher than {your_name}'s STR")

    else:
        yourpoint += 1
        print(f" • {your_name}'s STR, is higher than {player_name}'s DEF")

    if playertotaldex > yourtotaldex:
        playerpoint += 1
        print(f" • {player_name}'s DEX, is higher than {your_name}'s DEX")

    else:
        yourpoint += 1
        print(f" • {your_name}'s DEX, is higher than {player_name}'s DEX")

    if playerpoint > yourpoint:
        print(f"\nResult | Winner: {player_name} | {playerpoint} / {yourpoint}")
    elif playerpoint == yourpoint:
        print(f"\nResult | Draw | {playerpoint} / {yourpoint}")
    else:
        print(f"\nResult | Winner: {your_name} | {yourpoint} / {playerpoint}")
    

    print(command_menu)
    command = int(input())
    menu(command)

def guildTarget(target_id):
    clear()
    warrior_count = 0
    const_npc = 20
    const_pvp = 130
    const_step = 3
    print(build)
    

    targetinfo_endpoint = f'https://api.simple-mmo.com/v1/guilds/info/{target_id}?api_key={api_key}'
    targetinfo_response = requests.post(targetinfo_endpoint)
    host_endpoint = f'https://api.simple-mmo.com/v1/player/me?api_key={api_key}'
    host_response = requests.post(host_endpoint)

    host_guild = host_response.json()['guild']['id']
    host_name = host_response.json()['guild']['name']

    yourguild_endpoint = f'https://api.simple-mmo.com/v1/guilds/info/{host_guild}?api_key={api_key}'
    yourguild_response = requests.post(yourguild_endpoint)    
    yourguildmember_endpoint = f'https://api.simple-mmo.com/v1/guilds/members/{host_guild}?api_key={api_key}'
    yourguildmmeber_response = requests.post(yourguildmember_endpoint)

    target_name = targetinfo_response.json()['name']
    target_exp = targetinfo_response.json()['current_season_exp']

    host_name = yourguild_response.json()['name']
    host_exp = yourguild_response.json()['current_season_exp']
    host_members = yourguild_response.json()['member_count']
    difference = target_exp-host_exp
    if difference <= -1:
        difference = 0

    for i in range (host_members):
        member_warrior = yourguildmmeber_response.json()[i]['warrior']
        if member_warrior == 1:
            warrior_count += 1
    print(f"Calculating the Difference between {target_name} & {host_name}\n")
    print(f"Target Guild: {target_name}\nExperience: {number_formatting.format(target_exp)}\n")
    print(f"Your Guild: {host_name}\nExperience: {number_formatting.format(host_exp)}\n")
    print(f"Members: {host_members} | Warriors: {warrior_count}\n")
    print(f"Difference / Target: {number_formatting.format(difference)}\n")
    stepstotal = int(difference/const_step)
    npctotal = int(difference/const_npc)
    pvptotal = int(difference/const_pvp)

    stepsper = int(stepstotal/host_members)
    npcper = int(npctotal/host_members)
    pvpper = int(pvptotal/warrior_count)

    print(f"Total Steps Needed: {number_formatting.format(stepstotal)}\nTotal NPC Kills needed: {number_formatting.format(npctotal)}\nTotal PVP Kills needed: {number_formatting.format(pvptotal)}\n")
    print(f"Steps per member: {number_formatting.format(stepsper)}\nNPC Kills per member: {number_formatting.format(npcper)}\nPVP kills per warrior: {number_formatting.format(pvpper)} | Warriors: {warrior_count}")

    print(f"\nNote that this only calculates for the snapshot taken at the time of: {time.ctime()}.")
    print(f"\n{command_menu}")
    command = int(input())
    menu(command)
def menu(command):
    clear()
    if command == 1:
        sgl()
    if command == 2:
        clear()
        print(build)
        print(f"Input the ID of the guild you'd like to take a further look into.")
        print(warn_menu)
        guild_id = int(input())
        guild_specific(guild_id)
    if command == 3:
        clear()
        print(build)
        print("Which player would you like to check (input ID):")
        print(warn_menu)
        player_id = int(input())
        simulation(player_id)
    if command == 4:
        clear()
        print(build)
        print("What's your target guild (Guild ID Needed)?")
        print(warn_menu)
        target_id = int(input())
        guildTarget(target_id)
        
    if command == 0:
        print(build)
        print("Goodbye!")
        time.sleep(1)

print(command_menu)
command = int(input())
menu(command)
