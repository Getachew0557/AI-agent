# Handles Gemini API integration
import google.generativeai as genai
from config import GEMINI_API_KEY

def generate_code_gemini(prompt, language="python"):
    genai.configure(api_key=GEMINI_API_KEY)
    try:
        model = genai.GenerativeModel("gemini-pro")
        full_prompt = f"Generate {language} code:\n{prompt}"
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
