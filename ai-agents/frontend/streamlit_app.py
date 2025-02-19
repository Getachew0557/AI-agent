# frontend/streamlit_app.py
import streamlit as st
import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.model import generate_code_gemini
from chat.chatbot import chat_with_gemini
from utils.language_support import SUPPORTED_LANGUAGES
from utils.code_explainer import explain_code  # Import code explanation functionality

def main():
    st.title("🚀 AI Code Generator & Chatbot")

    tab1, tab2 = st.tabs(["Code Generator", "AI Chatbot"])

    # Code Generator Tab
    with tab1:
        st.header("Generate Code with AI")
        user_prompt = st.text_area("Describe what you want to generate:")
        language = st.selectbox("Select Programming Language", list(SUPPORTED_LANGUAGES.keys()))
        
        if st.button("Generate Code"):
            if user_prompt:
                st.write("Generating code...")
                generated_code = generate_code_gemini(user_prompt, SUPPORTED_LANGUAGES[language])
                
                if generated_code:
                    st.subheader("Generated Code:")
                    st.code(generated_code, language=SUPPORTED_LANGUAGES[language])
                    
                    # Code Explanation
                    explanation = explain_code(generated_code)
                    st.subheader("Code Explanation:")
                    st.write(explanation)

                    # Save Code Feature
                    st.download_button(
                        label="Download Code",
                        data=generated_code,
                        file_name=f'generated_code.{SUPPORTED_LANGUAGES[language]}',
                        mime='text/plain'
                    )
                else:
                    st.error("Failed to generate code. Please try again.")
            else:
                st.error("Please enter a coding request.")

    # AI Chatbot Tab
    with tab2:
        st.header("Ask AI Code Queries")
        user_query = st.text_area("Enter your coding question:")
        
        if st.button("Ask AI"):
            if user_query:
                st.write("AI is thinking...")
                ai_response = chat_with_gemini(user_query)
                
                if ai_response:
                    st.subheader("AI Response:")
                    st.write(ai_response)
                else:
                    st.error("Failed to get a response from AI. Please try again.")
            else:
                st.error("Please enter a question.")

if __name__ == "__main__":
    main()
