# 軽量なPythonイメージ
FROM python:3.9

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y git

# 作業ディレクトリの設定
WORKDIR /app

# AI専用フォルダからファイルをコピー
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリのコピー
COPY . .

# サーバー起動（HF Space用）
CMD ["python", "app.py"]
