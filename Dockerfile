FROM python:3.10-slim
RUN apt-get update && apt-get install -y git
RUN pip install requests GitPython
WORKDIR /app
# 起動時にGitHubから最新コードを取得して実行する
CMD git clone https://github.com/ai20260226-hue/local-AI-nation.git . && python main.py
