import gradio as gr
import os
import uuid
import shutil
import re
from transformers import AutoModel, AutoTokenizer

# Load GOT-OCR model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True)
model = AutoModel.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True, low_cpu_mem_usage=True, device_map='cpu', use_safetensors=True)
model = model.eval()

UPLOAD_FOLDER = "./uploads"
RESULTS_FOLDER = "./results"

# Ensure directories for uploads and results
for folder in [UPLOAD_FOLDER, RESULTS_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Function to run OCR on uploaded image
def run_GOT(image, search_term):
    unique_id = str(uuid.uuid4())
    image_path = os.path.join(UPLOAD_FOLDER, f"{unique_id}.png")
    
    # Save the uploaded image
    shutil.copy(image, image_path)
    
    try:
        # Run OCR in plain text mode, which will handle multiple languages
        res = model.chat(tokenizer, image_path, ocr_type='ocr')
        
        # Highlight search term in the result
        highlighted_text = highlight_text(res, search_term)
        
        return highlighted_text, None
    except Exception as e:
        return f"Error: {str(e)}", None
    finally:
        # Clean up the image after processing
        if os.path.exists(image_path):
            os.remove(image_path)

# Function to highlight search term in text
def highlight_text(text, search_term):
    if not search_term:
        return text
    pattern = re.compile(re.escape(search_term), re.IGNORECASE)
    return pattern.sub(lambda m: f'<span style="background-color: yellow;">{m.group()}</span>', text)

# Gradio Interface
title_html = """
<h2> <span class="gradient-text" id="text">General OCR Theory (GOT)</span>: Multi-Language OCR (English & Hindi)</h2>
"""

with gr.Blocks() as demo:
    gr.HTML(title_html)
    gr.Markdown("""
    ### Instructions
    Upload your image below and click "Submit" to extract text in both English and Hindi. You can also enter a word or phrase to highlight in the extracted text.
    """)

    # Upload and output interface
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="filepath", label="Upload your image")
            search_input = gr.Textbox(label="Enter a word or phrase to search", placeholder="Search term")
            submit_button = gr.Button("Submit")
        
        with gr.Column():
            ocr_result = gr.HTML(label="Extracted Text")

    # Connect the submit button with the OCR function
    submit_button.click(run_GOT, inputs=[image_input, search_input], outputs=[ocr_result])

# Launch the demo
if __name__ == "__main__":
    demo.launch()

    