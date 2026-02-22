from aiohttp.web import get
from dotenv import load_dotenv
import os
import requests

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not NEWS_API_KEY:
    raise ValueError("NEWS_API_KEY is not set in the environment variables.")

def get_global_news():
    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "category": "business",
        "language": "en",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }

    res = requests.get(url, params=params)

    return res.json().get("articles", [])
