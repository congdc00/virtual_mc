import gradio as gr
def init_ui():
    text_input = gr.Textbox()
    text_output = gr.Textbox()
    text_button = gr.Button("Flip")