## NEWS_AUTO_MANAGER

### 概要
このプロジェクトは最新のニュースを自動的に収集、要約し、トレンドを把握を促進するためのツールです。
主にビジネス関連のニュースを対象に集めています。

### 開発方法
1. このプロジェクトをクローンしてください
2. `uv sync --frozen`を実行してください。まだ`uv`がない場合は、公式ドキュメントを参照して導入してください
3. `env.example`をコピーして`.env`ファイルを作成し、必要な環境変数を設定してください
4. `Google AI Studio`でAPIキーを取得し、`GEMINI_API_KEY`のバリューに設定してください
5. `NEWSAPI`でAPIキーを取得し、`NEWS_API_KEY`のバリューに設定してください
6. メッセージを送りたい`Discord`のサーバーのurlを`WEBHOOK_URL`のバリューに設定してください

### 使用方法
GitHub Actionsを使用して、毎朝7:00(日本時間)にスクリプトが走るようにしています。
時間の調整は`workflows/daily_news.yml`の`cron`セクションで行うことができます。
クローンしたリポジトリの`settings`から`Secrets and variables` -> `Actions` -> `New repository secret`で、`.env`ファイルに記載した環境変数を設定してください。