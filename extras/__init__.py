import gradio as gr

def change_fc(choice):
    if choice=="Swapper":
        return gr.update(visible=False), gr.update(visible=True)
    elif choice=="Remove background":
        return gr.update(visible=False), gr.update(visible=False)
    elif choice=="Enhancer":
        return gr.update(visible=True), gr.update(visible=False) 
    elif choice=="Interpolate Video":
        return gr.update(visible=False), gr.update(visible=False)
    else:
        return gr.update(visible=False), gr.update(visible=False)

def change_resize(choice):
    if choice=="Scale":
        return gr.update(visible=True, interactive=True), gr.update(visible=False)
    else:
        return gr.update(visible=False), gr.update(visible=True)

def init_ui():
    video_path = gr.Video(label="Video input")
    type_function = gr.Dropdown(["Remove background", "Enhancer", "Swapper", "Interpolate Video"], label="Choose the function you want to use.")

    with gr.Column(visible=False) as row_swapper:
        with gr.Row():
            with gr.Column():
                choice_01 = gr.Radio(["Face", "Lip"], label="Body Parts", info="Select the body part you want to change")
                choice_02 = gr.Checkbox(label="Enhancer")
                with gr.Accordion("Advance setting", open=False):
                    model = gr.Dropdown(["GFP-Gan", "Model2"], value="Facefusion", label="Model", info="Select the model to use", interactive=True)
                    checkpoint = gr.Dropdown(["Checkpoint 01", "Checkpoint 02"], value="Checkpoint 01", label="Checkpoint", info="Select the checkpoint to use", interactive=True)
            image_01 = gr.Image(label="Image input")
        
    with gr.Column(visible=False) as row_enhancer:
        resize = gr.Checkbox(label="Enable Resize")
        type_resize = gr.Radio(["Scale", "Coordinate"], value="Scale", label="Type resize", interactive=True)

        scale = gr.Slider(0, 10, value=2, label="Scale", info="Choose between 0 and 10", visible=False)
        with gr.Row(visible=False) as coordinate:
            x_top = gr.Number(label="X_top")
            y_top = gr.Number(label="Y_top")
            x_bot = gr.Number(label="X_bot")
            y_bot = gr.Number(label="Y_bot")
        type_resize.change(fn=change_resize, inputs=type_resize, outputs=[scale, coordinate])
        with gr.Accordion("Advance setting", open=False):
            model = gr.Dropdown(["Real-ESRGAN", "GFP-Gan", "DiffBIR"], value="Real-ESRGAN", label="Model", info="Select the model to use", interactive=True)
            checkpoint = gr.Dropdown(["Checkpoint 01", "Checkpoint 02"], value="Checkpoint 01", label="Checkpoint", info="Select the checkpoint to use", interactive=True)

    type_function.change(fn=change_fc, inputs=type_function, outputs=[row_enhancer, row_swapper])


    convert_button = gr.Button("Convert")
    video_output = gr.Video(label="Result",interactive=False)