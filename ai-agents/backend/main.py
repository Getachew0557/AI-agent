# backend/main.py
import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.main import generate_code_gemini
from utils.language_support import SUPPORTED_LANGUAGES

def main():
    print("Welcome to AI Code Generator!")
    user_prompt = input("Enter your coding request: ")
    
    print("Choose a programming language:")
    for i, lang in enumerate(SUPPORTED_LANGUAGES.keys(), start=1):
        print(f"{i}. {lang}")
    
    lang_choice = input("Enter choice: ")
    language = list(SUPPORTED_LANGUAGES.keys())[int(lang_choice) - 1]
    
    print("\nGenerating code with Gemini...")
    gemini_code = generate_code_gemini(user_prompt, language)
    print(f"\nGenerated Code ({language}):\n{gemini_code}")

if __name__ == "__main__":
    main()
