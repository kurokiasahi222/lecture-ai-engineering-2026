# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：`glossary_search_glossary`
- STEP 2 の [tool call]：`glossary_search_glossary({'query': '3レベル'})`
- STEP 3 の [tool call]：`fetch_fetch({'url': 'https://modelcontextprotocol.io/'})`
- STEP 4 の [tool call]：`aws_aws___search_documentation({'topics': ['general'], 'search_phrase': 'Amazon S3 versioning overview'})`
- 気づき・疑問：`fetch_fetch` の説明文には「このツールでインターネットに接続できるようになった」というモデル向けの指示があり、サーバーの作者が書いた文がそのままモデルに渡ると分かった。STEP 4 では、回答の最後に根拠のない「関係する回：第1回」が付いた（INSTRUCTIONS の「関係する回を示す」が、AWS の質問にも効いている）。

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル：発展
- やったこと：Claude Code の MCP サーバーの設定方法を公式ドキュメントで調べ、演習の `app/mcp_servers.json` と比べた（調べた日：2026-11-28、参照：https://code.claude.com/docs/en/mcp ）
- 結果：

| 調べること | Claude Code | 演習の `app/mcp_servers.json` |
|---|---|---|
| 設定を書く場所 | `claude mcp add` で登録する。local・user スコープは `~/.claude.json`、project スコープはプロジェクト直下の `.mcp.json` に保存される | `app/mcp_servers.json` に手で書く |
| コマンドで起動する書き方 | `claude mcp add <名前> -- <コマンド> [引数...]`。JSON では `"command"`・`"args"`・`"env"` を書く（`"type"` を省くと stdio として扱われる） | `"command"`・`"args"`（`"env"` も書ける） |
| URL で接続する書き方 | `claude mcp add --transport http <名前> <URL>`。JSON では `"type": "http"` と `"url"` を書く | `"url"` だけ |
| 有効になる範囲 | `--scope` で選ぶ。local（既定）は自分だけ・このプロジェクトだけ、project は `.mcp.json` をリポジトリに入れて共有、user は自分のすべてのプロジェクト | このリポジトリの `app/mcp_agent.py` だけ |

- 気づき・疑問：Claude Code は `"type"` で接続方法を決めるので、演習の `"aws": {"url": …}` をそのまま `.mcp.json` に書くと設定エラーになる（`"type": "http"` が必要）。また Claude Code は対話モードでは、リポジトリの `.mcp.json` にあるサーバーを使う前に承認を求める。演習のエージェントは、設定ファイルにあるサーバーを確認なしで起動する。
