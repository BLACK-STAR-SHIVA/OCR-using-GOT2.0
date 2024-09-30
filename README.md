---
title: DEKHO
emoji: 💻
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: true
license: other
short_description: An OCR and Document Search Web Application.
---

###Qwen2-VL-2B-Instruct: Multi-Language OCR
Project Description
This project is a web application that performs Optical Character Recognition (OCR) on uploaded images, targeting text in both English and Hindi. It allows users to upload an image, extract text, and search keywords from the text.

Prerequisites
(Optional)NVIDIA GPU and Driver is installed
Python 3.7 or later installed.
(Optional)Set up a virtual environment python -m venv ocr venv\Scripts\activate
Setup Instructions
[All this Code is for windows only]

Clone the git Repository git clone https://github.com/BLACK-STAR-SHIVA/OCR-using-Qwen2-VL-2B-Instruct cd OCR-using-Qwen2-VL-2B-Instruct

(Optional)Set up a virtual environment python -m venv ocr venv\Scripts\activate

Install dependencies: pip install -r requirements.txt

Run the application: python app.py

Important Notes
--The system is using CPU now so the process can be slow upto minutes.(Because of not Enough Resources)

--The Code is made to run or CPU but it can be Modified for you if you are using GPU you can uncomment the line 39 and proceed to execute.

Model Information
This application utilizes the CPU version of the Qwen2-VL-2B-Instruct model for optical character recognition (OCR). The model is loaded from the Hugging Face model hub as follows:

Model: Qwen/Qwen2-VL-2B-Instruct Processor: AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct") Although the code includes functions for initializing a GPU version of the model, the deployed version exclusively uses the CPU model due to the limitations of the Hugging Face deployment environment. This choice may lead to slower processing times compared to a GPU-enabled version. However, it ensures compatibility across various deployment scenarios, including environments without GPU support.

By relying on the CPU model, the application maintains accessibility for a wider range of users while still delivering effective multi-language text extraction capabilities

Features
--Multi-Language Support: Capable of extracting text in multiple languages, specifically English and Hindi, to cater to a diverse user base.

--User-Friendly Interface: Built with Gradio, providing an intuitive and interactive web interface for seamless user interactions.

--Image Upload and Capture: Users can upload images or capture them using their webcam for OCR processing.

--Text Extraction: The application extracts text from images using the Qwen2-VL model, offering advanced capabilities in optical character recognition.

--Customizable Keyword Search: Users can input any word or phrase to search within the extracted text, making the search functionality flexible.

--Highlighting Matches: The application visually highlights occurrences of the search term in the extracted text, improving user experience and ease of reading.

--Responsive Design: The web application is responsive, ensuring a good user experience on both desktop and mobile devices.

--Error Handling: Provides user-friendly error messages in case of issues during text extraction or file upload, improving reliability.

--Cross-Platform Compatibility: Designed to run in any environment, including cloud platforms, due to its reliance on CPU for model execution.

User Experience
--Interactive Elements: The interface includes buttons for extracting text and searching for keywords, providing an engaging user experience.

--Advanced Styling: The application features modern design elements for buttons and inputs, enhancing visual appeal and usability.

Thanks
