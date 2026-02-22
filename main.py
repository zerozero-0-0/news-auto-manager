from func.summarize_news import summarize_news
from func.get_global_news import get_global_news

def main():
    articles = get_global_news()
    summary = summarize_news(articles)
    print(summary)


if __name__ == "__main__":
    main()
