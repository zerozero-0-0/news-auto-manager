from dotenv import load_dotenv
import os
import requests
from interfaces.data import COREDATA

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not NEWS_API_KEY:
    raise ValueError("NEWS_API_KEY is missing.")

def get_global_news():
    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "category": "business",
        "language": "en",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }



    res = requests.get(url, params=params)
    payload = res.json()

    # print(payload)

    data = []

    for p in payload["articles"]:
        current_data = COREDATA(
            title=p["title"],
            description=p["description"],
            url=p["url"]
        )
        data.append(current_data)
    
    return data

if __name__ == "__main__":
    result = get_global_news()
    for item in result:
        print(item)