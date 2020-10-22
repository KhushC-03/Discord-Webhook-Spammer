import os, random, time, sys, json
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord_webhook import DiscordWebhook
os.system('cls')
i = 0
f = open('webhook.json')
data = json.load(f)
wh = (data['webhook'])
def main():
    print("""\x1b[1;37m
    ____  _                   _ ___                  ___      _   
    |   \(_)___ __ ___ _ _ __| / __|_ __  __ _ _ __ | _ ) ___| |_ 
    | |) | (_-</ _/ _ \ '_/ _` \__ \ '_ \/ _` | '  \| _ \/ _ \  _|
    |___/|_/__/\__\___/_| \__,_|___/ .__/\__,_|_|_|_|___/\___/\__|
                                    |_|                            
    """)
    I0 = input("What do you want to say? ")
    I1 = input('How many times would you like to spam? ')
    for i in range(int(I1)):
        url = (wh)
        webhook = DiscordWebhook(url=url, content=IO)
        response = webhook.execute()
    main()
main()
