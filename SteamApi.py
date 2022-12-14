import requests
import random

steamApiKey = "YOUR-STEAM-API-KEY"
steamID = "YOUR-STEAM-USER-ID"

#Steam API link formatting for "GetOwnedGames"
slink1 = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
slink2 = "&steamid=" + steamID + "&include_appinfo=1&format=json"
slink = slink1 + steamApiKey + slink2

#Sent API Get request and save respond to a variable
r = requests.get(slink)

#convert to JSON and save to another variable
steam = r.json()

#JSON output with information about each game owned
print(steam)
#https://developer.valvesoftware.com/wiki/Steam_Web_API#GetOwnedGames_.28v0001.29

#Getting integer value of total games owned
totalGames = str(steam["response"]["game_count"])

#Output total games owned
print(totalGames)


#Some logic for getting a random game from account with over 10 hours playtime
steamGame = ""
steamGames = []

for num,item in enumerate (steam["response"]["games"]):
    num+=1
    if item["playtime_forever"] > 600:
        steamGame = item["name"]
        steamGames.append(steamGame)
    
steamRec = "".join((random.sample(steamGames, k=1)))

print(steamRec)
