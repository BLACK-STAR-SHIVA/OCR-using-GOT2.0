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

# General OCR Theory (GOT): Multi-Language OCR

## Project Description

This project is a web application that performs Optical Character Recognition (OCR) on uploaded images, targeting text in both English and Hindi.
It allows users to upload an image, extract text, and search keywords from the text.

## Prerequisites

- NVIDIA GPU and Driver is installed
- Python 3.7 or later installed.
- (Optional)Set up a virtual environment
  python -m venv ocr
  venv\Scripts\activate

## Setup Instructions

[All this Code is for windows only]

- Clone the git Repository
  git clone <repository_url>
  cd <repository_directory>

- (Optional)Set up a virtual environment
  python -m venv ocr
  venv\Scripts\activate

- Install dependencies:
  pip install -r requirements.txt

- Run the application:
  python app.py

### Features

Multi-Language Support: Capable of extracting text in multiple languages, specifically English and Hindi, to cater to a diverse user base.

Customizable Search: Users can input any word or phrase to search within the extracted text, making the search functionality flexible.

Highlighting Matches: The application visually highlights all occurrences of the search term in the extracted text, improving user experience and ease of reading.

User-Friendly Interface: Built with Gradio, providing an intuitive and interactive web interface for seamless user interactions.

Temporary Image Storage: Automatically creates a temporary directory for storing uploaded images, ensuring that the original files remain unaffected.

Error Handling: Provides user-friendly error messages in case of issues during text extraction or file upload, improving reliability.

Cross-Platform Compatibility: Designed to run in any environment, including cloud platforms, due to its reliance on CPU for the model execution.

Batch Processing: (If applicable) Allows multiple images to be uploaded and processed in one go, making it efficient for users needing to extract text from several images at once.

Output Formatting Options: Users can receive extracted text in different formats, such as plain text or JSON, depending on their requirements.

Responsive Design: The web application is responsive, ensuring a good user experience on both desktop and mobile devices.

### Model Information

This application utilizes the CPU version of the GOT (General OCR Theory) model for optical character recognition (OCR). The model is loaded from the Hugging Face model hub as follows:

Model: ucaslcl/GOT-OCR2_0
Tokenizer: ucaslcl/GOT-OCR2_0
Although the code includes functions for initializing a GPU version of the model, the deployed version exclusively uses the CPU model due to the limitations of the Hugging Face deployment environment. This choice may lead to slower processing times compared to a GPU-enabled version. However, it ensures compatibility across various deployment scenarios, including environments without GPU support.

By relying on the CPU model, the application maintains accessibility for a wider range of users while still delivering effective multi-language text extraction capabilities.