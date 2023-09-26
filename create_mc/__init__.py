import gradio as gr

def change_pose_box(choice):
    if choice == "video":
        return gr.update(lines=1, visible=True, label = "Video path", interactive = True)
    elif choice == "speech":
        return gr.update(lines=1, visible=True, label = "Speech path", interactive = True)
    else:
        return gr.update(visible=False)

def change_video_box(choice):
    if choice == "image":
        return gr.update(lines=1, visible=True, label = "Image path", interactive = True)
    elif choice == "promt":
        return gr.update(lines=8, visible=True, label = "Promt", interactive = True)
    else:
        return gr.update(visible=False)

def init_ui():
    with gr.Row():
        radio_pose = gr.Radio(
            ["video", "speech"], label="Bạn muốn lấy thông tin về pose từ đâu ?")

        radio_video = gr.Radio(
            ["image", "promt"], label="Bạn muốn lấy thông tin về character từ đâu ?")
    
    gr.Markdown("Nhập dữ liệu")
    pose_text = gr.Textbox(visible=False)
    radio_pose.change(fn=change_pose_box, inputs=radio_pose, outputs=pose_text)

    video_text = gr.Textbox(visible=False)
    radio_video.change(fn=change_video_box, inputs=radio_video, outputs=video_text)

    image_button = gr.Button("Create")