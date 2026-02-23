import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = -1002453264440  # твой ID

text = "✅ ТЕСТ: бот успешно публикует в канал"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHANNEL,
        "text": text
    }
)

print(response.text)
