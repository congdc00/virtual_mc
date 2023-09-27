import gradio as gr
def change_check_box(type_function):
    if type_function == "Face Swapper":
        return gr.update(visible=True, interactive=True)
    else:
        return gr.update(visible=False)
def init_ui():
    type_function = gr.Dropdown(["Enhancer", "Face Swapper"], label="Lựa chọn chức năng muốn sử dụng")
    with gr.Column():
        video_path = gr.Textbox(label="Video path")
        face_path = gr.Textbox(label="Image path",info="Ảnh chứa khuôn mặt mục tiêu" , visible=False)
        type_function.change(fn=change_check_box, inputs=type_function, outputs=face_path)
    convert_button = gr.Button("Convert")