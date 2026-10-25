"""第1回: 素のLLMに質問するスクリプト。

使い方:
    uv run python -m app.ask "LoRAとは何ですか？"
    uv run python -m app.ask            # 質問を省略すると、講座に固有の質問をする
    uv run python -m app.ask --chat     # 会話履歴を保ったまま続けて質問する（exit で終了）

ツールを持たない「素の」呼び出し。--chatなしでは会話履歴も持たない。
--chatではそれまでのやり取りを全て送り直して会話を続ける。
講座に固有のことを聞くと、「分からない」と答えるか、一般論でもっともらしく答える
（講座の実際とは違う）ことを確かめよう。
（第3回で、用語集を検索できるエージェントにして改善する）
"""

import argparse

from google import genai
from google.genai import errors, types

from app.config import MODEL, api_error_message, get_api_key

# 講座に固有の質問。正しい答えは data/glossary.json の homework-levels にある
DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"


def show_usage(response) -> None:
    usage = response.usage_metadata
    if usage:
        print(
            f"[トークン数] 入力 {usage.prompt_token_count} / 出力 {usage.candidates_token_count}"
        )


def ask(question: str) -> str:
    client = genai.Client(api_key=get_api_key())
    response = client.models.generate_content(model=MODEL, contents=question)
    show_usage(response)

    return response.text


def ask_and_answer(
    client: genai.Client, history: list[types.Content], question: str
) -> None:
    user_turn = types.UserContent(question)
    try:
        response = client.models.generate_content(
            model=MODEL, contents=history + [user_turn]
        )
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        return
    print(f"AI> {response.text}")
    print()
    history.append(user_turn)
    history.append(response.candidates[0].content)
    show_usage(response)


def chat(question: str | None) -> None:
    client = genai.Client(api_key=get_api_key())
    history = []
    print("Instruction: Type exit or quit to quit the program")
    print()
    try:
        if question:
            print(f"> {question}")
            ask_and_answer(client, history, question)
        while True:
            question = input("> ")
            question = question.strip()
            if question == "quit" or question == "exit":
                break
            if question == "":
                continue
            ask_and_answer(client, history, question)

    except (EOFError, KeyboardInterrupt):
        print()


def main() -> None:
    parser = argparse.ArgumentParser(description="素のLLMに質問する")
    parser.add_argument("question", nargs="?", default=None)
    parser.add_argument(
        "--chat",
        action="store_true",
        help="Chatモードに入る。会話履歴を保ったまま続けて質問できるようにする",
    )
    args = parser.parse_args()
    print(f"[model] {MODEL}")

    if args.chat:
        chat(args.question)
        return
    question = args.question if args.question else DEFAULT_QUESTION
    print(f"[質問] {question}\n")

    try:
        print(ask(question))
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
