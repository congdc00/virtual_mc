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
            gr.Checkbox(label="Enable", value=True)
            gr.Textbox(label="Promt")
        with gr.Tab(label="Image"):
            gr.Checkbox(label="Enable")
            gr.Image(label="Input Image")
        with gr.Column():
            gr.Image(label="Example", interactive=False)
            gr.Button("Example")
        
    with gr.Accordion("Advance setting", open=False):
        model = gr.Dropdown(["Latent Diffusion", "Stabel diffusion 1.0", "Stable diffusion 2.0", "Diffusers"], value="Stable diffusion 2.0", label="Model", info="Select the model to use", interactive=True)
        checkpoint = gr.Dropdown(["Checkpoint 01", "Checkpoint 02"], value="Checkpoint 01", label="Checkpoint", info="Select the checkpoint to use", interactive=True)
    
    btn_generater = gr.Button("Generater")
    gr.Video(label="Result", interactive=False)