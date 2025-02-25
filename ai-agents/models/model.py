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

