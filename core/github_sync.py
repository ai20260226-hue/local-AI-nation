import os
import requests
import base64
import json

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "ai20260226-hue"
REPO_NAME = "local-AI-nation"

BASE_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


def get_file(path):
    url = f"{BASE_URL}/contents/{path}"
    r = requests.get(url, headers=HEADERS)

    if r.status_code == 200:
        data = r.json()
        content = base64.b64decode(data["content"]).decode()
        return content, data["sha"]

    return None, None


def update_file(path, content, message="update from AI"):
    url = f"{BASE_URL}/contents/{path}"

    _, sha = get_file(path)

    payload = {
        "message": message,
        "content": base64.b64encode(content.encode()).decode(),
        "branch": "main"
    }

    if sha:
        payload["sha"] = sha

    r = requests.put(url, headers=HEADERS, data=json.dumps(payload))
    return r.status_code
