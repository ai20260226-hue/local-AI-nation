from core.github_sync import get_file, update_file


MEMORY_PATH = "nation/zaibatsu/memory.md"


def load_memory():
    content, _ = get_file(MEMORY_PATH)
    return content if content else ""


def save_memory(text):
    update_file(MEMORY_PATH, text, "update memory")
