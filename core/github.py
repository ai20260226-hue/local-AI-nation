import os
from github import Github

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = "ai20260226-hue/local-AI-nation"

def get_repo():
    g = Github(GITHUB_TOKEN)
    return g.get_repo(REPO_NAME)

def read_memory(path):
    repo = get_repo()
    file = repo.get_contents(path, ref="memory")
    return file.decoded_content.decode()

def write_memory(path, content, message="AI memory update"):
    repo = get_repo()
    try:
        file = repo.get_contents(path, ref="memory")
        repo.update_file(
            path=path,
            message=message,
            content=content,
            sha=file.sha,
            branch="memory"
        )
    except:
        repo.create_file(
            path=path,
            message=message,
            content=content,
            branch="memory"
        )
