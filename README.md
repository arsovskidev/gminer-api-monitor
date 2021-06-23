# gminer-api-monitor

![](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Farsovskidev%2Fgminer-api-monitor&count_bg=%23A4B6F7&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)

###### Create virtual environment and install requirements.

```
$ sudo apt-get install python3-venv
$ python3 -m venv gminer-api-monitor
$ source gminer-api-monitor/bin/activate
$ touch .env
$ pip3 install -r requirements.txt
$ python3 main.py
```

###### In the .env file enter the following settings.

```
$ nano .env

GMINER_API = [YOUR GMINER API]
TELEGRAM_BOT_API = [YOUR BOT API]
TELEGRAM_CHAT_ID = [YOUR CHAT ID]

```
