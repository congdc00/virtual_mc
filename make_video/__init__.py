import gradio as gr

def change_source(choice):
    if choice=="Upload":
        return gr.update(visible=True, interactive=True), gr.update(visible=True, interactive=True)
    else:
        return gr.update(visible=False), gr.update(visible=False)

def change_config(choice):
    if choice==True:
        return gr.update(visible=True), gr.update(visible=True, interactive=True), gr.update(visible=True, interactive=True), gr.update(visible=True, interactive=True), gr.update(visible=True, interactive=True)
    else:
        return gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def init_ui():
    type_source = gr.Radio(["Pre step", "Upload"],label="Source", info="Select source")
    with gr.Row():
        video_input = gr.Video(label="Video Input", visible=False)
        audio_input = gr.Audio(label="Speech Input", visible=False)

    with gr.Accordion("Setting", open=False):
        with gr.Row():
            config = gr.Checkbox(label="Pads")
            gr.Checkbox(label="Smooth", value=True, interactive=True)
        with gr.Row():
            title_pad = gr.Markdown("Pads setting", visible=False)
            x_top = gr.Number(label="X_top", visible=False)
            y_top = gr.Number(label="Y_top", visible=False)
            x_bot = gr.Number(label="X_bot", visible=False)
            y_bot = gr.Number(label="Y_bot", visible=False)
        config.change(fn=change_config, inputs=config, outputs=[title_pad, x_top, y_top, x_bot, y_bot])

    with gr.Accordion("Advance setting", open=False):
        model = gr.Dropdown(["Model 01", "Model 02"], value="Model 01", label="Model", info="Select the model to use", interactive=True)
        model = gr.Dropdown(["Checkpoint 01", "Checkpoint 02"], value="Checkpoint 01", label="Checkpoint", info="Select the checkpoint to use", interactive=True)

    type_source.change(fn=change_source, inputs=type_source, outputs=[video_input, audio_input])
    convert_button = gr.Button("Generate")
    
    audio_output = gr.Video(interactive=False)
