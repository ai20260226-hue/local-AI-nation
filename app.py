import gradio as gr

def status():
    return "AI Nation is alive and stable."

demo = gr.Interface(fn=status, inputs=None, outputs="text")

if __name__ == "__main__":
    demo.launch()
