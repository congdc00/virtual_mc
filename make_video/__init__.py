import gradio as gr
def init_ui():
    video_path = gr.Textbox(lines = 1, interactive = True, label="Video path")
    speech_path = gr.Textbox(lines = 1, interactive = True, label="Speech path")
    gr.Checkbox(label="Enhancer", info="Scale up video")