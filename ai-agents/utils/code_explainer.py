import google.generativeai as genai
from config import GEMINI_API_KEY

def explain_code(code):
    genai.configure(api_key=GEMINI_API_KEY)
    try:
        model = genai.GenerativeModel("gemini-pro")
        prompt = f"Explain this code in detail:\n{code}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating explanation: {str(e)}"
