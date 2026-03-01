import gradio as gr
from core.github import write_memory, read_memory

def test_memory():
    write_memory("memory/reports/test.md", "Nation memory test")
    return read_memory("memory/reports/test.md")

demo = gr.Interface(fn=test_memory, inputs=None, outputs="text")

if __name__ == "__main__":
    demo.launch()
