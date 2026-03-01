import gradio as gr

def test():
    return "AI Nation Stable"

demo = gr.Interface(fn=test, inputs=None, outputs="text")

if __name__ == "__main__":
    demo.launch()
