import gradio as gr

def change_source_pose(choice):
    if choice=="Video":
        return gr.update(visible=True, interactive=True), gr.update(visible=False)
    elif choice=="Speech":
        return gr.update(visible=False), gr.update(visible=True, interactive=True)

def init_ui():
    gr.Markdown("<h1 align='center'> Part 2: Create MC </h1>")
    with gr.Accordion("Tutorials", open=False):
        gr.Markdown("Step 1: Upload the data containing MC's poses.")
        gr.Markdown("Step 2: (Optional) Enter a prompt or an image for the desired output -> Press enable")
        gr.Markdown("Step 3: Press the 'Generate' button and wait for the result.")

    type_source_pose = gr.Dropdown(["Video", "Speech"], value="Video", label="Source pose", info="Select the source pose to use", interactive=True)
    source_pose_video = gr.Video(label="Input video", visible=False)
    source_pose_audio = gr.Audio(label="Input Audio", visible=False, type="filepath")

    type_source_pose.change(fn=change_source_pose, inputs=type_source_pose, outputs=[source_pose_video, source_pose_audio])
    with gr.Row():
        with gr.Tab(label="Promt"):
            gr.Checkbox(label="Enable", value=True)
            gr.Textbox(label="Promt")
        with gr.Tab(label="Image"):
            gr.Checkbox(label="Enable")
            gr.Image(label="Input Image", type="filepath")
        with gr.Column():
            gr.Image(label="Example", interactive=False, type="filepath")
            gr.Button("Example")
        
    with gr.Accordion("Advance setting", open=False):
        model = gr.Dropdown(["Latent Diffusion", "Stabel diffusion 1.0", "Stable diffusion 2.0", "Diffusers"], value="Stable diffusion 2.0", label="Model", info="Select the model to use", interactive=True)
        checkpoint = gr.Dropdown(["Checkpoint 01", "Checkpoint 02"], value="Checkpoint 01", label="Checkpoint", info="Select the checkpoint to use", interactive=True)
    
    btn_generater = gr.Button("Generater")
    gr.Video(label="Result", interactive=False)