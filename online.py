from config import *
import json
import time
import websocket
import requests
import hashlib


def load_config_file(filename):
    with open(filename, "r") as f:
        json_data = json.load(f)
    return json_data


def hash_json(json_data):
    return hashlib.sha256(json.dumps(json_data).encode("utf-8")).hexdigest()


config_data = load_config_file("./config.json")
config_hash = hash_json(config_data)

userinfo = requests.get(
    "https://discordapp.com/api/v9/users/@me",
    headers={"Authorization": config_data["token"], "Content-Type": "application/json"},
).json()


username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]
auth = {
    "op": 2,
    "d": {
        "token": config_data["token"],
        "properties": {
            "$os": "Arch Linux",
            "$browser": "Google Chrome",
            "$device": "Arch Linux",
        },
        "presence": {"status": config_data["status"], "afk": False},
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
                "state": config_data["custom_status"],
                "name": "Custom Status",
                "id": "custom",
                "emoji": {
                    "name": config_data["emoji_name"],
                    "id": config_data["emoji_id"],
                    "animated": config_data["isAnimatedEmoji"],
                },
            }
        ],
        "status": config_data["status"],
        "afk": False,
    },
}
online = {"op": 1, "d": "None"}


def keep_online():
    ws = websocket.WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
    start = json.loads(ws.recv())
    heartbeat = start["d"]["heartbeat_interval"]
    ws.send(json.dumps(auth))
    ws.send(json.dumps(cstatus))
    time.sleep(heartbeat / 1000)
    ws.send(json.dumps(online))


def run_keep_online():
    global config_hash
    print(f"staying alive for {username}#{discriminator} , user_id = {userid}.")
    while True:
        config_data = load_config_file("./config.json")
        if hash_json(config_data) != config_hash:
            config_hash = hash_json(config_data)
            status = config_data["status"]
            cstatus["d"]["activities"][0]["state"] = config_data["status"]
            cstatus["d"]["activities"][0]["emoji"]["name"] = config_data["emoji_name"]
            cstatus["d"]["activities"][0]["emoji"]["id"] = config_data["emoji_id"]
            cstatus["d"]["activities"][0]["emoji"]["animated"] = config_data[
                "isAnimatedEmoji"
            ]
            cstatus["d"]["status"] = config_data["status"]
            print("Config file updated")
        keep_online()
        time.sleep(30)


run_keep_online()
