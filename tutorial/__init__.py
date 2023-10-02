import gradio as gr
def init_ui():
    gr.Markdown("""<h1 align='center'> Chào mừng đến với Virtual MC HG Media </h1>""")
    with open("./tutorial/tutorial.html", "r") as file:
        html_content = file.read()
    gr.Markdown(f"""{html_content}
                """)