import requests
import time
import os
clear = lambda: os.system('cls')
clear()

print("Please input your API key, which can be found in https://web.simple-mmo.com/p-api/home")
api_key = input()
clear()

host_endpoint = f'https://api.simple-mmo.com/v1/player/me?api_key={api_key}'
host_response = requests.post(host_endpoint)


guild_ID = host_response.json()['guild']['id']
guild_NAME = host_response.json()['guild']['name']
print(f"{guild_ID} | {guild_NAME}\n")

guildmember_endpoint = f'https://api.simple-mmo.com/v1/guilds/members/{guild_ID}?api_key={api_key}'
guildmember_response = requests.post(guildmember_endpoint)

print("How long is your inactivity range (in days)")
inactivity_range = int(input())
print(f"Checking for inactive members ({inactivity_range} days inactivity.)")
def inactive():
        for i in range(80):
                try:
                        member_name = guildmember_response.json()[i]['name']
                        member_id = guildmember_response.json()[i]['level']
                        member_inactive = guildmember_response.json()[i]['last_activity']
                        current_time = time.time()
                        inactivity_time = inactivity_range * 86400
                        calculation = current_time-inactivity_time
                        days_inactive1 = current_time-member_inactive
                        days_inactive2 = days_inactive1/86400
                        days_inactive_int = int(days_inactive2)

                        if calculation >= member_inactive:
                                print(f"{member_id} | {member_name} | {time.ctime(member_inactive)} | {days_inactive_int} days inactive.")

                except:
                        continue       


inactive()

gmr = guildmember_response.headers["X-RateLimit-Remaining"]
print(gmr)