import gradio as gr
def init_ui():
    with gr.Group():
        gr.Textbox(label="First")
        gr.Textbox(label="Last")
    gr.Checkbox(label="Enhancer", info="Scale up video")