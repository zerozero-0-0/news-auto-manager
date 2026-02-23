from func.summarize_news import summarize_news
from func.get_global_news import get_global_news
from func.send_message_to_url import send_message_to_url

def main():
    articles = get_global_news()
    summary = summarize_news(articles)
    send_message_to_url(summary)


if __name__ == "__main__":
    main()
