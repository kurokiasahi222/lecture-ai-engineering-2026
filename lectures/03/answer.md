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
```
発展
```
- やったこと：
```
(a) 演習のエージェントと同じ指示とツールを使い、エージェントを組み立てる部分だけを Google の ADK で書き直し、adk run で動かして、書き方や回答を比べる
```
- 結果：
```
===== AIE2026の講座の宿題にある「3レベル」とは何ですか？

----- Pydantic AI
[model] gemini-3.5-flash-lite
AIE2026の講座における「3レベル」とは、宿題の構成を示す3つの段階のことです。

具体的には以下の3つのレベルに分かれており、ご自身の学習目標やペースに合わせて**どれか1つ**に取り組めば、その回の宿題は完了となります。

1. **基礎**：講義内容の確認
2. **実装**：自分でコードを書く
3. **発展**：調査や試行

なお、原則として宿題の採点はありませんので、ご自身の理解度や興味に合わせて無理のないレベルを選んで取り組んでみてください。

（関連：第1回）

--- trace ---
[tool call]   search_glossary({'query': '3レベル'})
[tool return] search_glossary -> [{"term": "宿題の3レベル", "lecture": 1, "definition": "AIE2026の宿題の構成。「基礎（講義内容の確認）」「実装（自分でコードを書く）」「発展（調査や試行）」の3段階があり、どれか1つに取り組…
[usage] RunUsage(cost=Decimal('0.0006631'), details={'text_prompt_tokens': 927}, input_text_tokens=927, input_tokens=927, output_tokens=154, requests=2, tool_calls=1)

----- ADK
[tool call]   search_glossary({"query":"3レベル"})
[tool return] search_glossary -> [{"term": "宿題の3レベル", "lecture": 1, "definition": "AIE2026の宿題の構成。「基礎（講義内容の確認）」「実装（自分でコードを書く）」「発展（調査や試行）」の3段階があり、どれか1つに取り組…
[glossary_agent]: AIE2026講座における「3レベル」とは、各回の宿題の難易度や取り組み方の構成を指す言葉です。

具体的には以下の3つの段階に分かれています。

1. **基礎**：講義内容の確認（インプットの定着）
2. **実装**：自分でコードを書く（手を動かす演習）
3. **発展**：調査や試行（より深い応用・発展的な内容）

受講にあたっては、この3つのうち**どれか1つ**に取り組めばその回の宿題は完了となります。なお、原則として採点は行われません。
```
```
===== LoRAとQLoRAの違いは？

----- Pydantic AI
[model] gemini-3.5-flash-lite
LoRAとQLoRAの主な違いは、**ベースモデルの重みをそのまま使うか、量子化して縮小するか**という点にあります。

* **LoRA（Low-Rank Adaptation）**
  事前学習済みの重み（元のモデル）を固定したまま、重みの更新分を低ランク行列で近似し、その小さな行列（アダプタ）だけを学習するPEFT（Parameter-Efficient Fine-Tuning）手法です。学習パラメータや保存ファイルを大幅に削減できます。

* **QLoRA（Quantized LoRA）**
  LoRAの仕組みをベースにしつつ、**ベースモデルの重みを4ビットなどに量子化（低精度化）**してメモリ消費をさらに劇的に節約する手法です。これにより、より大きなモデルを比較的小さなGPUメモリでも効率よく学習・ファインチューニングできるようになります。

（関連する回：第2回）

--- trace ---
[tool call]   search_glossary({'query': 'LoRA'})
[tool call]   search_glossary({'query': 'QLoRA'})
[tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…
[tool return] search_glossary -> [{"term": "QLoRA", "lecture": 2, "definition": "ベースモデルの重みを4ビットなどに量子化してメモリを節約したうえで、LoRAで学習する手法。より大きなモデルを小さなGPUで扱える。本講座の第2…
[usage] RunUsage(cost=Decimal('0.0009895'), details={'text_prompt_tokens': 1340}, input_text_tokens=1340, input_tokens=1340, output_tokens=235, requests=2, tool_calls=2)

----- ADK
[tool call]   search_glossary({"query":"LoRA"})
[tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…
[glossary_agent]: LoRAとQLoRAの違いは、ベースモデルの重みの保持方法（精度）と、それに伴う必要なメモリ量にあります。

* **LoRA（Low-Rank Adaptation）**
  事前学習済みの重みを固定したまま、低ランクの小さな行列（アダプタ）のみを追加・学習するPEFT（Parameter-Efficient Fine-Tuning）手法です。学習パラメータを大幅に削減できます。
* **QLoRA（Quantized LoRA）**
  LoRAの手法をベースにしつつ、ベースモデルの重みを4ビットなどの**量子化（Quantization）**によって極限まで圧縮・軽量化してから学習を行う手法です。これにより、より大きなモデルでも、限られたGPUメモリで効率よくファインチューニングできるようになります。

（関連する回：第2回）
```
```
===== 第2回の内容から確認問題を1問出して

----- Pydantic AI
[model] gemini-3.5-flash-lite
第2回の内容から確認問題を出題します！

**【問題】**
「Hugging Face Hub」とはどのようなものか、説明してください。

（第2回）

--- trace ---
[tool call]   make_quiz({'lecture': 2})
[tool return] make_quiz -> {"question": "「Hugging Face Hub」の意味は?", "answer": "公開されたモデルやデータセットを共有・ダウンロードできるプラットフォーム。オープンウェイトのモデルを入手したり、LoRAアダプタを公開した…
[usage] RunUsage(cost=Decimal('0.0003895'), details={'text_prompt_tokens': 865}, input_text_tokens=865, input_tokens=865, output_tokens=52, requests=2, tool_calls=1)

----- ADK
[tool call]   make_quiz({"lecture":2})
[tool return] make_quiz -> {"question": "「教師ありファインチューニング（SFT）」の意味は?", "answer": "入力と望ましい出力のペア（例：質問と模範回答）を使ってモデルを追加学習させる方法。指示に従う振る舞いを身につけさせる代表的な手法。"…
[glossary_agent]: 第2回の内容から確認問題を1問出題します！

**【確認問題】**
「教師ありファインチューニング（SFT）」の意味は何でしょうか？

正解だと思う内容を考えてみてくださいね。
（関連：第2回）
```
- 気づき・疑問：
```
基本的には自装のエージェントでもGoogle ADKを使ったエージェントでも答えにあまり違いは見られなかった。
```
