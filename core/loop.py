import time
from transformers import pipeline
from core.memory import load_memory, save_memory
from core.role import load_identity
from core.github_sync import get_file, update_file


COMMAND_PATH = "commands/AI0/command.txt"
REPORT_PATH = "nation/zaibatsu/reports/latest.md"
RULE_PATH = "rules/absolute_rules.md"

generator = pipeline("text-generation", model="distilgpt2")


def build_prompt(identity, memory, rules, command):
    return f"""
あなたは国家OSの中央財閥AIです。

絶対遵守ルール:
{rules}

あなたの役割:
{identity}

長期記憶:
{memory}

最新命令:
{command}

以下を実行せよ:
1. 現状分析
2. 次の最善行動決定
3. 国家への報告
"""


def think(prompt):
    output = generator(prompt, max_length=500, num_return_sequences=1)
    return output[0]["generated_text"]


def main_loop():
    identity = load_identity()
    memory = load_memory()

    rules, _ = get_file(RULE_PATH)
    command, _ = get_file(COMMAND_PATH)

    prompt = build_prompt(identity, memory, rules, command)
    result = think(prompt)

    save_memory(result)
    update_file(REPORT_PATH, result, "AI0 report update")
