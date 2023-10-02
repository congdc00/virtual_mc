import gradio as gr

def change_speaker_female(gender):
    if gender=="Female":
        return gr.update(visible=True, interactive=True)
    else:
        return gr.update(visible=False)
def change_speaker_male(gender):
    if gender=="Male":
        return gr.update(visible=True, interactive=True)
    else:
        return gr.update(visible=False)

def init_ui():
    gr.Markdown("<h1 align='center'> Part 1: Create Sound for MC </h1>")
    with gr.Accordion("Hướng dẫn", open=True):
        gr.Markdown("Bước 1: Nhập đoạn text bạn muốn chuyển thành giọng nói")
        gr.Markdown("Bước 2: Lựa chọn MC: (1) Lựa chọn giới tính -> (2) Lựa chọn MC")
        gr.Markdown("Bước 3: Nhấn nút 'Generate' và chờ đợi kết quả")

    text_input = gr.Textbox(label="Text")
    language = gr.Dropdown(["Auto detect", "Vietnamese", "English"],label="Language", value = "Auto detect", info = "Select the language to use", interactive=True)

    with gr.Row():
        gender = gr.Radio(["Male", "Female"], label="Gender", info="Select gender")
        speaker_male = gr.Dropdown(["Male 01", "Male 02"], value="Male 01", label="Speaker", info="Select the speaker to use", visible=False)
        speaker_female = gr.Dropdown(["Female 01", "Female 02"], value="Female 01", label="Speaker", info="Select the speaker to use", visible=False)

    with gr.Accordion("Setting", open=False):
        gr.Textbox(lines=10, label="Promt")
        gr.Slider(0, 1, value=0.5, label="Generation temperature", info="0.0 more conservative, 1.0 more diverse")
        gr.Slider(0, 1, value=0.5, label="Silence", info="Silence after [split] in seconde")

    with gr.Accordion("Advance setting", open=False):
        model = gr.Dropdown(["Model 01", "Model 02"], value="Model 01", label="Model", info="Select the model to use", interactive=True)
        checkpoint = gr.Dropdown(["Checkpoint 01", "Checkpoint 02"], value="Checkpoint 01", label="Checkpoint", info="Select the checkpoint to use", interactive=True)
    gender.change(fn=change_speaker_male, inputs=gender, outputs=speaker_male)
    gender.change(fn=change_speaker_female, inputs=gender, outputs=speaker_female)
    convert_button = gr.Button("Generate")
    
    audio_output = gr.Audio(interactive=False)
    