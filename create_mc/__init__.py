import gradio as gr

def change_source_pose(choice):
    if choice=="Video":
        return gr.update(visible=True, interactive=True), gr.update(visible=False)
    elif choice=="Speech":
        return gr.update(visible=False), gr.update(visible=True, interactive=True)

def init_ui():

    type_source_pose = gr.Dropdown(["Video", "Speech"], value="Video", label="Source pose", info="Select the source pose to use", interactive=True)
    source_pose_video = gr.Video(label="Input video", visible=False)
    source_pose_audio = gr.Audio(label="Input Audio", visible=False)

    type_source_pose.change(fn=change_source_pose, inputs=type_source_pose, outputs=[source_pose_video, source_pose_audio])
    with gr.Row():
        with gr.Tab(label="Promt"):
            gr.Checkbox(label="Enable")
            gr.Textbox(label="Promt")
        with gr.Tab(label="Image"):
            gr.Checkbox(label="Enable")
            gr.Image(label="Input Image")
        with gr.Column():
            gr.Image(label="Example", interactive=False)
            gr.Button("Example")
    image_button = gr.Button("Generater")

    gr.Video(label="Result", interactive=False)