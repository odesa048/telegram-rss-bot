import feedparser
import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = -1002453264440
RSS_URL = "https://www.048.ua/rss"

feed = feedparser.parse(RSS_URL)

if not feed.entries:
    exit()

post = feed.entries[0]

text = f"📰 {post.title}\n\n{post.link}"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
requests.post(
    url,
    data={
        "chat_id": CHANNEL,
        "text": text,
        "disable_web_page_preview": False,
    },
)
