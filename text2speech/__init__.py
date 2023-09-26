import gradio as gr
def init_ui():
    text_input = gr.Textbox(label="Text")
    audio_output = gr.Audio()
    convert_button = gr.Button("Convert")