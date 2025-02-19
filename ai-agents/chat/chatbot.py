# AI Chatbot for code queries
import google.generativeai as genai
from config import GEMINI_API_KEY

def chat_with_gemini(query):
    genai.configure(api_key=GEMINI_API_KEY)
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
