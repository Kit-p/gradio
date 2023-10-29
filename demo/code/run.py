import gradio as gr
import os
from time import sleep

# Load CSS file
css_file = os.path.join(os.path.dirname(__file__), "file.css")

# Function to set code language and return a Code block
def set_lang(language):
    print(language)
    return gr.Code(language=language)

# Function to set code language from a file path
def set_lang_from_path():
    sleep(1)
    return gr.Code((css_file,), language="css")

# Function to display code in a specified language
def code(language, code):
    return gr.Code(code, language=language)

# Create a Gradio interface for code input and output
io = gr.Interface(lambda x: x, "code", "code")

# Create a Gradio interface for the code demo
with gr.Blocks() as demo:
    # Dropdown to select programming language
    lang = gr.Dropdown(value="python", choices=gr.Code.languages)
    with gr.Row():
        # Code input block
        code_in = gr.Code(
            language="python",
            label="Input",
            value='def all_odd_elements(sequence):\n    """Returns every odd element of the sequence."""',
        )
        # Code output block
        code_out = gr.Code(label="Output")
    # Buttons for running code and loading from a file
    btn = gr.Button("Run")
    btn_two = gr.Button("Load File")

    # Define interactions based on button clicks and language selection
    lang.change(set_lang, inputs=lang, outputs=code_in)
    btn.click(code, inputs=[lang, code_in], outputs=code_out)
    btn_two.click(set_lang_from_path, inputs=None, outputs=code_out)

    # Render the Gradio interface
    io.render()

if __name__ == "__main__":
    # Launch the code demo
    demo.launch()
