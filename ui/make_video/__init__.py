import gradio as gr
from make_video.processing import wav2lip

def change_model(choice):
    if choice=="Wav2Lip":
        return gr.update(visible=True, interactive=True), gr.update(visible=False)
    else:
        return gr.update(visible=False), gr.update(visible=True, interactive=True)

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
    gr.Markdown("<h1 align='center'> Part 3: Aggregate results from speech and MC pose </h1>")
    with gr.Accordion("Hướng dẫn", open=True):
        gr.Markdown("Bước 1: Tải lên dữ liệu video và image mà bạn muốn sử dụng (Có thể chọn Pre-step nếu bạn muốn sử dụng kết quả ở Part I & II)")
        gr.Markdown("Bước 2: Tùy chỉnh cấu hình theo nhu cầu của bạn")
        gr.Markdown("Bước 3: Nhấn nút generater và chờ đợi kết quả")

    type_source = gr.Radio(["Pre step", "Upload"],value="Upload", label="Source", info="Select source", interactive=False)
    with gr.Row():
        video_input = gr.Video(label="Video Input", visible=True, width=360, height=360)
        audio_input = gr.Audio(label="Speech Input", visible=True, type="filepath")

    with gr.Accordion("Setting", open=False):
        with gr.Row():
            config = gr.Checkbox(label="Pads", value=False)
            smooth = gr.Checkbox(label="Smooth", value=True, interactive=True)
            face_enhancer = gr.Checkbox(label="Face Enhance", value=False, interactive=True)
            frame_enhancer = gr.Checkbox(label="Frame Enhance", value=False, interactive=True)
        with gr.Row():
            title_pad = gr.Markdown("Pads setting", visible=False)
            x_top = gr.Number(label="X_top", visible=False)
            y_top = gr.Number(label="Y_top", visible=False)
            x_bot = gr.Number(label="X_bot", visible=False)
            y_bot = gr.Number(label="Y_bot", visible=False)
        config.change(fn=change_config, inputs=config, outputs=[title_pad, x_top, y_top, x_bot, y_bot])
    
    with gr.Accordion("Advance setting", open=False):
        model = gr.Dropdown(["Wav2Lip", "Lip-sync"], value="Wav2Lip", label="Model", info="Select the model to use", interactive=True)
        checkpoints_w2l = gr.Dropdown(["wav2lip", "wav2lip_gan", "lipsync_expert", "visual_quality_disc"], value="wav2lip", label="Checkpoint", info="Select the checkpoint to use", interactive=True)
        checkpoints_diffbur = gr.Dropdown(["default"], value="default", label="Checkpoint", info="Select the checkpoint to use", interactive=True, visible=False)
        model.change(fn=change_model, inputs=model, outputs=[checkpoints_w2l, checkpoints_diffbur])
    
    type_source.change(fn=change_source, inputs=type_source, outputs=[video_input, audio_input])
    button = gr.Button("Generate")
    with gr.Row():
        result = gr.Video(label="AVideo Result",interactive=False, width=360, height=720)
        video_example = gr.Video(label="AiClip Example", width=360, height=720)
    button.click(wav2lip, inputs=[model, video_input, audio_input, smooth, config, x_top, y_top, x_bot, y_bot, face_enhancer, frame_enhancer], outputs=[result])
    with gr.Row():
        gr.Examples(
            [["Wav2Lip", "wav2lip","./data/example/make_video/vid_01.mp4", "./data/example/make_video/audio_01.mp3", "./data/example/make_video/example_01.mp4"], 
             ["Wav2Lip", "wav2lip","./data/example/make_video/vid_02.mp4", "./data/example/make_video/audio_02.mp3", "./data/example/make_video/example_02.mp4"], 
             ["Wav2Lip", "wav2lip","./data/example/make_video/vid_03.mp4", "./data/example/make_video/audio_03.mp3", "./data/example/make_video/example_03.mp4"]],
            [model, checkpoints_w2l, video_input, audio_input, video_example],
            result,
            wav2lip,
            cache_examples=False,
        )
    

    
