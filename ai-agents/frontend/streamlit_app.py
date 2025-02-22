# Streamlit Web UI for AI Code Generation and Debugging
import streamlit as st
import sys
import os
from PIL import Image

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.model import generate_code_gemini, debug_code_gemini
from chat.chatbot import chat_with_gemini
from utils.language_support import SUPPORTED_LANGUAGES
from utils.code_explainer import explain_code
from utils.vision_model import extract_text_from_image

def main():
    st.title("🚀 Multi-AI Agent Code Assistant")

    tab1, tab2, tab3 = st.tabs(["Code Generator", "AI Chatbot", "Image to Code"])

    # Code Generator Tab
    with tab1:
        st.header("Generate & Debug Code with AI")
        user_prompt = st.text_area("Describe what you want to generate:")
        language = st.selectbox("Select Programming Language", list(SUPPORTED_LANGUAGES.keys()))
        
        if st.button("Generate Code", key="generate_code"):
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

                    # Debugging Feature
                    if st.button("Debug Code", key="debug_code"):
                        st.write("Debugging code...")
                        debugged_code = debug_code_gemini(generated_code)
                        st.subheader("Debugged Code:")
                        st.code(debugged_code, language=SUPPORTED_LANGUAGES[language])

                else:
                    st.error("Failed to generate code. Please try again.")
            else:
                st.error("Please enter a coding request.")

    # AI Chatbot Tab
    with tab2:
        st.header("Ask AI Code Queries")
        user_query = st.text_area("Enter your coding question:")
        
        if st.button("Ask AI", key="ask_ai"):
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

    # Image to Code Tab
    with tab3:
        st.header("Upload an Image to Generate Code")
        uploaded_image = st.file_uploader("Upload an image (e.g., handwritten code, diagram)", type=["png", "jpg", "jpeg"])
        
        if uploaded_image:
            image = Image.open(uploaded_image)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            if st.button("Extract Text & Generate Code", key="extract_text_image"):
                extracted_text = extract_text_from_image(image)
                st.subheader("Extracted Text:")
                st.write(extracted_text)

                st.write("Generating code from extracted text...")
                generated_code = generate_code_gemini(extracted_text, "python")  # Default to Python
                
                if generated_code:
                    st.subheader("Generated Code:")
                    st.code(generated_code, language="python")

                    # Explanation
                    explanation = explain_code(generated_code)
                    st.subheader("Code Explanation:")
                    st.write(explanation)
                    
                    # Debugging Feature for extracted code
                    if st.button("Debug Extracted Code", key="debug_extracted_code"):
                        st.write("Debugging extracted code...")
                        debugged_code = debug_code_gemini(generated_code)
                        st.subheader("Debugged Code:")
                        st.code(debugged_code, language="python")

                else:
                    st.error("Failed to generate code. Please try again.")

if __name__ == "__main__":
    main()
