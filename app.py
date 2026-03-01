import gradio as gr
from core.github import read_memory, write_memory
import datetime

def nation_think():
    now = datetime.datetime.utcnow().isoformat()

    thought = f"""
## AI0 Report

Time: {now}

Nation is operating normally.
"""

    write_memory(
        "memory/reports/latest.md",
        thought,
        message="AI0 periodic report"
    )

    return thought


def show_memory():
    try:
        return read_memory("memory/reports/latest.md")
    except:
        return "No memory yet."


with gr.Blocks() as demo:
    gr.Markdown("# AI Nation – AI0")

    think_btn = gr.Button("Run Nation Cycle")
    output = gr.Markdown()

    memory_btn = gr.Button("Show Latest Memory")
    memory_output = gr.Markdown()

    think_btn.click(nation_think, outputs=output)
    memory_btn.click(show_memory, outputs=memory_output)

if __name__ == "__main__":
    demo.launch()
