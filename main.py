import os
from dotenv import load_dotenv
import requests
import time
import math

# Load environment (.env) settings.
load_dotenv()
GMINER_API = os.getenv("GMINER_API")
TELEGRAM_BOT_API = os.getenv("TELEGRAM_BOT_API")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Loop interval every 5 seconds.
time_interval = 5


def sendMessage(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_API}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&parse_mode=html&text={message}"
    requests.get(url)


def getStats():
    url = f"{GMINER_API}"
    try:
        response = requests.get(url)
        response_json = response.json()
        return response_json
    except requests.ConnectionError as e:
        return False


def checkStats():
    stats = getStats()
    if stats == False:
        sendMessage("Miner is down!")
    else:
        gpu = stats["devices"][0]["name"]
        temperature = stats["devices"][0]["temperature"]
        fan_speed = stats["devices"][0]["fan"]
        speed = stats["devices"][0]["speed"]

        if fan_speed < 50:
            sendMessage(
                f"[ {gpu} ]'s Fan is working slow! [Fan speed: {fan_speed}] [{temperature}°C]"
            )

        if temperature > 66:
            sendMessage(f"[ {gpu} ]'s Temperature is a bit high! [{temperature}°C]")
        if temperature < 50:
            sendMessage(
                f"[ {gpu} ]'s Temperature is low, something is going on! [{temperature}°C]"
            )

        if speed < 200000:
            sendMessage(f"[ {gpu} ]'s Hashrates are so slow! [{speed / 1000000}MH/s]")


# -----------------------------------------------------------------
# Main Loop


def main():
    while True:
        print("Getting DATA...")
        checkStats()
        time.sleep(time_interval)


if __name__ == "__main__":
    main()
