import numpy as np
import gradio as gr
import create_speech, make_video, create_mc, extras, tutorial



with gr.Blocks() as demo:
    gr.Markdown("<center><h1> Virtual MC </h1></center>")
    with gr.Tab("Welcome"):
        tutorial.init_ui()

    with gr.Tab("Extras"):
        extras.init_ui()

    with gr.Tab("Create speech"):
        create_speech.init_ui()

    with gr.Tab("Create MC"):
        create_mc.init_ui()

    with gr.Tab("Make Video"):
        make_video.init_ui()
        
    

demo.launch(share=False)