import requests
import os
clear = lambda: os.system('cls')
clear() # clears the terminal, used for debugging

print("Please input your API key, which can be found in https://web.simple-mmo.com/p-api/home")
api_key = input()
clear()
#for API calls = calling the endpoint, and getting the json file as a response.
diamond_market_endpoint = f'https://api.simple-mmo.com/v1/diamond-market?api_key={api_key}'
diamondmarket_response = requests.post(diamond_market_endpoint)
#api_key = used to input the users api token, to be implemented in the later stages

#function that handles diamond market checking
def diamond_market(checking_price): #checking_price compares in-game prices to the user's requested price
        numberOfEntry = 0 # inputs the number of retrieved entries, if left at 0, will print an error message.
        for i in range(1000): # checks the market, for the first 50 listings | pointer, which helps print the values that satisfy checking_price
                # prints the sellers details, such as name, id, diamonds remaining, and price
                try:
                        seller = diamondmarket_response.json()[i]['seller']['name']
                        remaining = diamondmarket_response.json()[i]['diamonds_remaining']
                        price = diamondmarket_response.json()[i]['price_per_diamond']

                        if price <= checking_price: # compares the prices and the user's checking price, and prints out listings that satisfy, else
                                numberOfEntry = i
                                print(f"USER {seller} REMAINING {remaining} PRICE {price}")
                                numberOfEntry += 1
                except:
                        continue

        if numberOfEntry <= 0: # prints that there are no listings for the user's budget
                        print(f"There are no diamonds equal to, or lower than {checking_price}")
                        print(f"Lowest listing is:\nUSER {seller} REMAINING {remaining} PRICE {price}")
print("Fleuren's SimpleMMO Diamond Listing Tool v1.0")
print("Search for diamonds at the highest value of:")

checking_price = int(input()) # takes the user input, and checks with the diamond_market function
diamond_market(checking_price)

print("\n")

rateLimit = diamondmarket_response.headers["X-RateLimit-Remaining"] # prints the current user's rate limit
print(f"Your API Credits (resets every minute): {rateLimit}")
