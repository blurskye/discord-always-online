# stay online forever
A python script that keeps your account online

## Requirements 
- [Python 3+](https://www.python.org/)
- [Discord](https://discord.com/) account. 

## Installation 🐍
### git clone this repo and change directory to this repo by running 

```sh
git clone https://github.com/blurskye/discord-always-online.git
cd discord-always-online.git
```

### install all dependencies by running this
```sh
python -m venv .venv
./.venv/bin/pip install -r requirement.txt
```

##keep in mind this install dependencies in a virtual python environment

# Edit config.py to add your config
# to get discord token, login into your discord account from browser, press f12, goto console and run this
```js
window.webpackChunkdiscord_app.push([
  [Math.random()],
  {},
  req => {
    for (const m of Object.keys(req.c)
      .map(x => req.c[x].exports)
      .filter(x => x)) {
      if (m.default && m.default.getToken !== undefined) {
        return copy(m.default.getToken());
      }
      if (m.getToken !== undefined) {
        return copy(m.getToken());
      }
    }
  },
]);
console.log('%cWorked!', 'font-size: 50px');
console.log(`%cYou now have your token in the clipboard!`, 'font-size: 16px');
```
##it will copy discord token to your clipboard, you need to paste that in token variable in config.py

_____________________________________________________________________________________________
# ⚠️⚠️⚠️
### DO NOT GIVE YOUR TOKEN TO OTHERS !!!
#### _Giving your token to someone else will give them the ability to log into your account without the password or 2FA._
> ❗ **Warning**
> : Self-bots are discouraged by Discord and is against Discord's ToS. You might get banned for this if not used properly.

> 📝 **Note**
> : Discord's Terms of Service: [discord.com/terms](https://discord.com/terms)

> This repository is in no way affiliated with, authorized, maintained, sponsored or endorsed by [Discord Inc.](https://discord.com/) or any of its affiliates or subsidiaries.

_____________________________________________________________________________________________
## Usage 🍕
```
./.venv/bin/python online.py
```
If you did all the steps correctly, you should see the following message on the console.

````
staying alive for {username}{discriminator} , user_id = {userid}Logged in as <you user name>
````