from google import genai
from interfaces.data import CoreData, DisplayData
import time
from constants import REQUEST_INTERVAL_SECONDS

def summarize_news(articles: list[CoreData]) -> list[DisplayData] | str:
    if not articles:
        return "ニュースが見つかりませんでした"

    client = genai.Client()

    outputs = []

    base_prompt = """
    以下の記事の内容を要約してください。要約は90以上120文字以下の日本語にしてください。
    回答のみを出力してください。だ・である調にして。
    """


    for article in articles:
        prompt = f"{base_prompt}\n\nタイトル: {article.title}\n説明: {article.description}"
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        assert response.text, "要約の生成に失敗しました"


        current_data = DisplayData(
            title=article.title,
            summary=response.text,
            url=article.url
        )
        outputs.append(current_data)
        time.sleep(REQUEST_INTERVAL_SECONDS) # 15回/1min なので本番は5sにする  

    return outputs


if __name__ == "__main__":
    from func.get_global_news import get_global_news
    news = get_global_news()
    outputs = summarize_news(news)
    for output in outputs:
        print(output)