import gradio as gr
from make_video.processing import process

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
        video_input = gr.Video(label="Video Input", visible=False, width=360, height=360)
        audio_input = gr.Audio(label="Speech Input", visible=False, type="filepath")

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
        model = gr.Dropdown(["Rudrabha", "Model 02"], value="Rudrabha", label="Model", info="Select the model to use", interactive=True)
        checkpoint = gr.Dropdown(["Wav2Lip", "Wav2Lip+GAN", "Expert Discriminator", "Visual Quality Discriminator"], value="Wav2Lip", label="Checkpoint", info="Select the checkpoint to use", interactive=True)

    type_source.change(fn=change_source, inputs=type_source, outputs=[video_input, audio_input])
    button = gr.Button("Generate")
    result = gr.Video(interactive=False)
    button.click(process, inputs=[checkpoint, video_input, audio_input], outputs=[result])
    
