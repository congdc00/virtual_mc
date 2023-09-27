import numpy as np
import gradio as gr
import data_processing, text2speech, make_video, create_mc, extras






with gr.Blocks() as demo:

    gr.Markdown("<center><h1> Virtual MC </h1></center>")

    with gr.Tab("Data Processing"):
        data_processing.init_ui()

    with gr.Tab("Create speech"):
        text2speech.init_ui()

    with gr.Tab("Create MC"):
        create_mc.init_ui()

    with gr.Tab("Make Video"):
        make_video.init_ui()

    with gr.Tab("Extras"):
        extras.init_ui()
        
    with gr.Accordion("Hướng dẫn"):
        gr.Markdown("Bước 1: ...")

demo.launch()