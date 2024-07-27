import json
import requests
import random
def print_out(name_, usr_, online_, url_, pic_):
    if name != 0:    
        print(f"Realname: {name_}")
    elif name == 0: pass
    print(f"Username: {usr_}")
    print(f"Activity: {online_}")
    print(f"URL: {url_}")
    print(f"Pic: {pic_}")
key = "" #!ACTUNG! insert you steam api key here
id = "76561197960435530" #insert here player id of whos profile info you're interested at
r = requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={id}")
result = json.loads(r.text)

online = result['response']['players'][0]['personastate']
if online == "1":
    online = "online"
else: online = "offline"
url = result['response']['players'][0]['profileurl']
usr = result['response']['players'][0]['personaname']
pic = result['response']['players'][0]['avatarfull']
try:
    name = result['response']['players'][0]['realname']
except:
    name = 0
r1 = requests.get(f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={key}&steamid={id}&relationship=friend")
result1 = json.loads(r1.text)
nonsense_ids = list()
# print(result1["friendslist"]["friends"])
print_out(name, usr, online, url, pic)

print("-------------------------------------------")
print("          User friends stats:")
x = 0
for i in result1["friendslist"]["friends"]: 
    if x == 10: break
    nonsense_ids.append(i["steamid"])
    x += 1
for i in nonsense_ids:
    r = requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={i}")
    result = json.loads(r.text)

    online = result['response']['players'][0]['personastate']
    if online == "1":
        online = "online"
    else: online = "offline"
    url = result['response']['players'][0]['profileurl']
    usr = result['response']['players'][0]['personaname']
    pic = result['response']['players'][0]['avatarfull']
    try:
        name = result['response']['players'][0]['realname']
    except:
        name = 0
    print_out(name, usr, online, url, pic)
owned_games = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&steamid=76561197960265731&format=json&include_appinfo=true")
owned_result = json.loads(owned_games.text)
game_count = owned_result["response"]["game_count"]
# print(owned_result)
games_ = list()
y = 0
for i in owned_result["response"]["games"]:
    if y == 10: break
    games_.append(i["name"])
    y += 1
print("10 owned games one of player friends(actually hardcoded, cuz not everyone\
 show their games on public)")
disposable = 1
for i in games_:
    if disposable == 1: 
        print("           Games list:")
        disposable += 1
    print(f"    {i}")
    