import requests
import random

TOKEN = ""
CHAT_ID = ""
MESSAGE = "hello from your telegram bot"
x = random.random()

# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MESSAGE}"

print(requests.get(url).json())