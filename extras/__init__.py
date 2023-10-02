import gradio as gr
from extras.rmbg import remove_bg
from extras.swapper import swap
from extras.enhancer import enhancer
def change_fc(choice):
    if choice=="Swapper":
        return gr.update(visible=False),gr.update(visible=False), gr.update(visible=True)
    elif choice=="Change background":
        return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)
    elif choice=="Enhancer":
        return gr.update(visible=False),gr.update(visible=True), gr.update(visible=False)
    elif choice=="Interpolate Video":
        return gr.update(visible=False),gr.update(visible=False), gr.update(visible=False)
    else:
        return gr.update(visible=False),gr.update(visible=False), gr.update(visible=False)

def change_resize(choice):
    if choice=="Scale":
        return gr.update(visible=True, interactive=True), gr.update(visible=False)
    else:
        return gr.update(visible=False), gr.update(visible=True)

def change_swap_face_input(list_choice):
    if "Face" in list_choice:
        return gr.update(visible=True,interactive=True)
    else:
        return gr.update(visible=False)

def change_swap_lip_input(list_choice):
    if "Lip" in list_choice:
        return gr.update(visible=True,interactive=True)
    else:
        return gr.update(visible=False)
def change_input_background(choice):
    if choice=="Upload":
        return gr.update(visible=True)
    else: 
        return gr.update(visible=False)
def change_input(choice):
    if choice=="Video":
        return gr.update(visible=True, interactive=True), gr.update(visible=False)
    else: 
        return gr.update(visible=False), gr.update(visible=True, interactive=True)
def init_ui():
    gr.Markdown("<h1 align='center'> Video Editing Auxiliary Tools </h1>")
    with gr.Accordion("Hướng dẫn", open=True):
        gr.Markdown("Bước 1: Nhấn vào video input và chọn video mà bạn muốn chỉnh sửa")
        gr.Markdown("Bước 2: Chọn loại chức năng mà bạn muốn sử dụng")
        gr.Markdown("Bước 3: (Option) Tùy chỉnh cấu hình cho phù hợp với nhu cầu")
        gr.Markdown("Bước 4: Nhấn nút Convert và chờ đợi kết quả")

    video_path = gr.Video(label="Video input", height=360)
    type_function = gr.Dropdown(["Change background", "Enhancer", "Swapper", "Interpolate Video"], label="Choose the function you want to use.")

    with gr.Column(visible=False) as row_bg:
        type_source = gr.Radio(["Transparent", "Upload"], value="Transparent", label="Type background", info="Select the background you want", interactive=True)
        with gr.Row(visible=False) as row_upload:
            type_upload = gr.Radio(["Video", "Image"], value="Video", label="Type source", info="Select the input you want", interactive=True)
            video_input = gr.Video(visible=True, interactive=True, width=360, height=360)
            image_input = gr.Image(visible=False, width=360, height=360, type="filepath")
            type_upload.change(fn=change_input, inputs=type_upload, outputs=[video_input, image_input])
        type_source.change(fn=change_input_background, inputs=type_source, outputs=row_upload)
        btn = gr.Button("Convert")
        video_output = gr.Video(label="Result",interactive=False, height=360)
        btn.click(remove_bg, inputs=[type_source, video_path, video_input], outputs=[video_output])
        gr.Examples(
            [["Transparent","./data/example/extras/rembg/vid_01.mp4"]],
            [type_source, video_path],
            video_output,
            remove_bg,
            cache_examples=False,
        )

    with gr.Column(visible=False) as row_swapper:
        with gr.Row():
            with gr.Column():
                choice_01 = gr.CheckboxGroup(["Face", "Lip"], label="Body Parts", info="Select the body part you want to change")
                choice_02 = gr.Checkbox(label="Enhancer")
                with gr.Accordion("Advance setting", open=False):
                    model = gr.Dropdown(["Facefusion", "Model2"], value="Facefusion", label="Model", info="Select the model to use", interactive=True)
                    checkpoint = gr.Dropdown(["Checkpoint 01", "Checkpoint 02"], value="Checkpoint 01", label="Checkpoint", info="Select the checkpoint to use", interactive=True)
            image_01 = gr.Image(label="Image input", visible=False, type="filepath")
            speech_01 = gr.Audio(label="Audio Input", visible=False, type="filepath")
            choice_01.change(fn=change_swap_face_input, inputs=choice_01, outputs=image_01)
            choice_01.change(fn=change_swap_lip_input, inputs=choice_01, outputs=speech_01)
        btn = gr.Button("Convert")
        video_output = gr.Video(label="Result",interactive=False, height=360)
        btn.click(swap, inputs=[choice_01, video_path, image_01, speech_01, choice_02], outputs=[video_output])
        gr.Examples(
            [[["Face", "Lip"],"./data/example/extras/swap/vid_01.mp4", "./data/example/extras/swap/target_face_01.png", "./data/example/extras/swap/audio_02.mp3", True], [["Face"],"./data/example/extras/swap/vid_02.mp4", "./data/example/extras/swap/target_face_02.png", "./data/example/extras/swap/audio_02.mp3", True], [["Lip"],"./data/example/extras/swap/vid_03.mp4", "./data/example/extras/swap/target_face_03.png", "./data/example/extras/swap/audio_02.mp3", True]],
            [choice_01, video_path, image_01, speech_01, choice_02],
            video_output,
            swap,
            cache_examples=False,
        )

    with gr.Column(visible=False) as row_enhancer:
        resize = gr.Checkbox(label="Enable Resize")
        type_resize = gr.Radio(["Scale", "Coordinate"], value="Scale", label="Type resize", interactive=True)

        scale = gr.Slider(0.1, 10, value=1, label="Scale", info="Choose between 0.1 and 10", visible=True, interactive=True)
        with gr.Row(visible=False) as coordinate:
            x_top = gr.Number(label="X_top")
            y_top = gr.Number(label="Y_top")
            x_bot = gr.Number(label="X_bot")
            y_bot = gr.Number(label="Y_bot")
        type_resize.change(fn=change_resize, inputs=type_resize, outputs=[scale, coordinate])
        with gr.Accordion("Advance setting", open=False):
            model = gr.Dropdown(["Real-ESRGAN", "GFP-Gan", "DiffBIR"], value="Real-ESRGAN", label="Model", info="Select the model to use", interactive=True)
            checkpoint = gr.Dropdown(["RealESRGAN_x4plus", "RealESRGAN_x4plus-anime"], value="RealESRGAN_x4plus", label="Checkpoint", info="Select the checkpoint to use", interactive=True)
        btn = gr.Button("Convert")
        video_output = gr.Video(label="Result",interactive=False, height=360)
        btn.click(enhancer, inputs=[video_path, scale], outputs=[video_output])
        gr.Examples(
            [["./data/example/extras/enhancer/vid_01.mp4",2]],
            [video_path, scale],
            video_output,
            enhancer,
            cache_examples=False,
        )
    type_function.change(fn=change_fc, inputs=type_function, outputs=[row_bg, row_enhancer, row_swapper])
    

    