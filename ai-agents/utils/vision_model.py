import pytesseract
import cv2
import numpy as np

def extract_text_from_image(image):
    """Extract text from an uploaded image using OCR."""
    image = np.array(image)
    text = pytesseract.image_to_string(image)
    return text.strip()

# Handles Gemini API integration for code generation and debugging
import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def generate_code_gemini(prompt, language="python"):
    """
    Generate code based on a user prompt using Gemini AI.
    """
    try:
        model = genai.GenerativeModel("gemini-pro")
        full_prompt = f"Generate {language} code:\n{prompt}"
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def debug_code_gemini(code):
    """
    Debug the given code and provide a corrected version using Gemini AI.
    """
    try:
        model = genai.GenerativeModel("gemini-pro")
        debug_prompt = f"Analyze the following code and fix any errors:\n\n```{code}```\n\nProvide a corrected version along with an explanation."
        response = model.generate_content(debug_prompt)
        return response.text
    except Exception as e:
        return f"Error debugging code: {str(e)}"

