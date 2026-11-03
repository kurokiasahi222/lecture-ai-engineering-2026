# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
```
エージェントはツールを使う。
素のLLMはツールを使わないので、外部の知識を使えない。
```
- `--trace` で見えたツール呼び出し（ツール名と引数）：
```
[tool call]   make_quiz({'lecture': 2})
[tool return] make_quiz -> {"question": "「Hugging Face Hub」の意味は?", "answer": "公開されたモデルやデータセットを共有・ダウンロードできるプラットフォーム。オープンウェイトのモデルを入手したり、LoRAアダプタを公開した…
```
- 1つの質問での LLM 呼び出し回数（`requests`）：
```
requests=2
[usage] RunUsage(cost=Decimal('0.0003845'), details={'text_prompt_tokens': 865}, input_text_tokens=865, input_tokens=865, output_tokens=50, requests=2, tool_calls=1)
```
- 追加したツールと、docstring に書いた説明：
```
追加したツール: make_quiz
docstring に書いた説明: 
"""指定した回の講義のクイズを出す。

    「第2回の内容から確認問題を出して」などのように、クイズの出題を聞かれたときに使う
"""
```

## 宿題

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：
