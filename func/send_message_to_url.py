from dotenv import load_dotenv
import os
from interfaces.data import DisplayData
import requests

load_dotenv()

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

def send_message_to_url(data: list[DisplayData] | str):
    if WEBHOOK_URL is None:
        raise ValueError("環境変数WEBHOOK_URLが設定されていません")
    
    if isinstance(data, str):
        print(data)
        return

    for each_data in data:
        embed = {
            "title": each_data.title,
            "description": f"```{each_data.summary}```",
            "url": each_data.url
        }

        payload = {
            "embeds": [embed]
        }

        res = requests.post(WEBHOOK_URL, json=payload)
        if res.status_code != 204:
            raise Exception(f"Failed to send message: {res.status_code}, {res.text}")
    

    
if __name__ == "__main__":
    from func.get_global_news import get_global_news
    from func.summarize_news import summarize_news

    news = get_global_news()
    summaries = summarize_news(news)
    send_message_to_url(summaries)