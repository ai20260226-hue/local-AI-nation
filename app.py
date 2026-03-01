import threading
import time
import gradio as gr

def background_loop():
    while True:
        print("Nation thinking...")
        time.sleep(30)

threading.Thread(target=background_loop, daemon=True).start()

def status():
    return "AI Nation is alive and stable."

demo = gr.Interface(fn=status, inputs=[], outputs="text")
demo.launch()
