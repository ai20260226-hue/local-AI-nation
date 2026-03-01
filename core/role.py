import json
from core.github_sync import get_file


IDENTITY_PATH = "nation/zaibatsu/identity.json"


def load_identity():
    content, _ = get_file(IDENTITY_PATH)
    return json.loads(content) if content else {}
