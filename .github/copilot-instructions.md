## NEWS-AUTO-MANAGER

## 概要
ビジネスや政治関連のニュースを自動で収集し、要約するためのプロジェクト

## 技術スタック
- Python 3.10
- newsapi
- gemini-2.5-flash-lite  // リクエストの制限が緩いため
- uv
  (以下、現時点では未導入)
- Docker
- GitHub Actions
- 

## プロジェクト構成
```
.
├── func
│   ├── __pycache__
│   ├── get_global_news.py // newsapiからニュースを取得する関数
│   └── summarize_news.py // geminiを用いてニュースを日本語に要約する関数
├── interfaces
│   ├── __pycache__
│   └── data.py // ニュースやデータのクラスの定義
├── LICENSE
├── main.py // エントリポイント func以下の関数を呼び出す
├── pyproject.toml 
├── README.md
└── uv.lock
```