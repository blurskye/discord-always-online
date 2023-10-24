import config
import json
import time
import websocket
import requests

status = "dnd"
token = config.token
custom_status = "Grinding"
emoji_id = "809138950118834197"
emoji_name = "polishcow"
isAnimatedEmoji = True
headers = {"Authorization": token, "Content-Type": "application/json"}
userinfo = requests.get(
    "https://discordapp.com/api/v9/users/@me", headers=headers
).json()
username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]


def keep_online(token, status):
    ws = websocket.WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
    start = json.loads(ws.recv())
    heartbeat = start["d"]["heartbeat_interval"]
    auth = {
        "op": 2,
        "d": {
            "token": token,
            "properties": {
                "$os": "Arch Linux",
                "$browser": "Google Chrome",
                "$device": "Arch Linux",
            },
            "presence": {"status": status, "afk": False},
        },
        "s": None,
        "t": None,
    }
    cstatus = {
        "op": 3,
        "d": {
            "since": 0,
            "activities": [
                {
                    "type": 4,
                    "state": custom_status,
                    "name": "Custom Status",
                    "id": "custom",
                    "emoji": {
                        "name": emoji_name,
                        "id": emoji_id,
                        "animated": isAnimatedEmoji,
                    },
                }
            ],
            "status": status,
            "afk": False,
        },
    }
    online = {"op": 1, "d": "None"}
    ws.send(json.dumps(auth))
    ws.send(json.dumps(cstatus))
    time.sleep(heartbeat / 1000)
    ws.send(json.dumps(online))


def run_keep_online():
    print(f"staying alive for {username}.")
    while True:
        keep_online(token, status)
        time.sleep(30)


run_keep_online()
