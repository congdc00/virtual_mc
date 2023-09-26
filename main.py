import numpy as np
import gradio as gr
import data_processing, text2speech
import make_video
import create_mc



def change_check_box(type_function):
    if type_function == "Face Swapper":
        return gr.update(visible=True, interactive=True)
    else:
        return gr.update(visible=False)


with gr.Blocks() as demo:

    gr.Markdown("<center><h1> Virtual MC </h1></center>")

    with gr.Tab("Data processing"):
        data_processing.init_ui()


    with gr.Tab("Create speech"):
        text2speech.init_ui()

    with gr.Tab("Create MC"):
        create_mc.init_ui()

    with gr.Tab("Make Video"):
        make_video.init_ui()

    with gr.Tab("Utils"):
        type_function = gr.Dropdown(["Enhancer", "Face Swapper"], label="Lựa chọn chức năng muốn sử dụng")
        
        with gr.Column():
            video_path = gr.Textbox(label="Video path")
            face_path = gr.Textbox(label="Image path",info="Ảnh chứa khuôn mặt mục tiêu" , visible=False)
            type_function.change(fn=change_check_box, inputs=type_function, outputs=face_path)
        convert_button = gr.Button("Convert")
        
    with gr.Accordion("Hướng dẫn"):
        gr.Markdown("Bước 1: ...")

demo.launch()