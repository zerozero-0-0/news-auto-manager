from google import genai


def summarize_news(articles):
    if not articles:
        return "ニュースが見つかりませんでした"

    client = genai.Client()
    output_blocks = []

    for idx, article in enumerate(articles, start=1):
        title = article.get("title") or "(タイトルなし)"
        description = article.get("description") or ""
        url = article.get("url") or ""

        prompt = f"""
            以下の英文ニュースを日本語で要約してください。

            要件:
            - 100字前後（目安: 90〜120字）
            - 余計な前置きは不要、要約本文のみを返す

            Title: {title}
            Description: {description}
        """

        res = client.models.generate_content(
            model="gemini-3-flash-preview", contents=prompt
        )

        summary = (res.text or "").strip()
        output_blocks.append(
            f"{idx}. タイトル: {title}\n   要約: {summary}\n   リンク: {url}"
        )

    return "\n\n".join(output_blocks)
