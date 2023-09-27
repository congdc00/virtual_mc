import gradio as gr
def init_ui():
    type_function = gr.Dropdown(["Enhancer", "Swapper", "Interpolate Video"], label="Lựa chọn chức năng muốn sử dụng")
    with gr.Column():
        video_path = gr.Textbox(label="Video path")
    convert_button = gr.Button("Convert")