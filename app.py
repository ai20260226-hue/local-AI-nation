import threading
import time
from flask import Flask

from core.loop import main_loop  # あなたの国家ループ

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Nation is alive and thinking."


def run_nation():
    while True:
        try:
            main_loop()
        except Exception as e:
            print("Loop error:", e)
        time.sleep(5)


if __name__ == "__main__":
    t = threading.Thread(target=run_nation)
    t.daemon = True
    t.start()

    app.run(host="0.0.0.0", port=7860)
