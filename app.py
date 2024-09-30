import gradio as gr
from PIL import Image
import torch
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor

# Load model and processor
model = Qwen2VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-VL-2B-Instruct",
    torch_dtype="auto",
    device_map="auto",
    ignore_mismatched_sizes=True  # Ignore config mismatches
)
processor = AutoProcessor.from_pretrained(
    "Qwen/Qwen2-VL-2B-Instruct"
)

# OCR extraction function
def extract_text_from_image(image):
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image"},
                {"type": "text", "text": "Extract text from the image(OCR)"}
            ]
        }
    ]

    text_prompt = processor.apply_chat_template(messages, add_generation_prompt=True)

    inputs = processor(
        text=[text_prompt],
        images=[image],
        padding=True,
        return_tensors="pt"
    )
    
    # Uncomment this line if GPU is available
    # inputs = inputs.to("cuda")

    # Reduce token generation for faster results
    output_ids = model.generate(**inputs, max_new_tokens=512)

    generated_ids = [
        output_ids[len(input_ids):]
        for input_ids, output_ids in zip(inputs.input_ids, output_ids)
    ]

    extracted_text = processor.batch_decode(
        generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True
    )[0]

    return extracted_text

# Keyword search function
def search_keyword(extracted_text, keyword):
    if not extracted_text:
        return "No text extracted. Please upload an image and run OCR first."
    
    if keyword:
        if keyword.lower() in extracted_text.lower():
            return f"Keyword '{keyword}' found in the extracted text."
        else:
            return f"Keyword '{keyword}' not found in the extracted text."
    return "Please enter a keyword to search."

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("<h1 style='text-align: center; color: #2c3e50;'>OCR with Keyword Search</h1>")
    
    # Step 1: Take photo and extract text
    img_input = gr.Image(type="pil", label="Upload or Capture Image for OCR")
    extract_btn = gr.Button("Extract Text", elem_id="extract-button")
    extracted_text = gr.Textbox(label="Extracted Text from OCR", lines=4, interactive=False)

    extract_btn.click(extract_text_from_image, inputs=[img_input], outputs=[extracted_text])
    
    # Step 2: Keyword search
    keyword_input = gr.Textbox(label="Enter keyword to search in extracted text", placeholder="Type your keyword here")
    search_btn = gr.Button("Search Keyword", elem_id="search-button")
    search_result = gr.Textbox(label="Keyword Search Result", lines=2, interactive=False)

    search_btn.click(search_keyword, inputs=[extracted_text, keyword_input], outputs=[search_result])

# Custom CSS for advanced styling
demo.css = """
body {
    font-family: 'Arial', sans-serif;
    background: linear-gradient(135deg, #ecf0f1, #bdc3c7);
    padding: 20px;
}

#extract-button {
    width: 150px;  
    height: 45px;  
    font-size: 16px; 
    background: linear-gradient(45deg, #4CAF50, #45a049); 
    color: white; 
    border: none; 
    border-radius: 5px; 
    cursor: pointer; 
    transition: background 0.3s, transform 0.3s; 
}

#extract-button:hover {
    background: linear-gradient(45deg, #45a049, #4CAF50); 
    transform: scale(1.05); 
}

#search-button {
    width: 150px;  
    height: 45px;  
    font-size: 16px; 
    background: linear-gradient(45deg, #008CBA, #007bb5); 
    color: white; 
    border: none; 
    border-radius: 5px; 
    cursor: pointer; 
    transition: background 0.3s, transform 0.3s; 
}

#search-button:hover {
    background: linear-gradient(45deg, #007bb5, #008CBA); 
    transform: scale(1.05); 
}

h1 {
    margin-bottom: 20px;
}

.gradio-container {
    border-radius: 10px; 
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    padding: 20px;
}

.textbox {
    border: 1px solid #bdc3c7; 
    border-radius: 5px; 
    padding: 10px;
}
"""

# Launch the Gradio app
demo.launch()
