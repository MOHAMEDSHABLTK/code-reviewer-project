import streamlit as st
import google.generativeai as genai

# Configure Google Gemini AI
API_KEY = "AIzaSyDvXPOIA88GNeQob8NVacZrUm-b2hy__do"
genai.configure(api_key=API_KEY)


def review_code(user_code):
    """Sends user code to Google Gemini AI for review and suggestions."""
    prompt = f"""
    Analyze the following Python code for potential bugs, errors, and improvements.
    Provide a structured report on issues found, categorize them, and suggest a corrected version of the code.

    **Code:**
    ```python
    {user_code}
    ```
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text


# Streamlit UI
st.set_page_config(page_title="AI Code Reviewer", page_icon="🔍", layout="wide")
st.title("🔍 AI Code Reviewer")
st.write("Submit your Python code below for AI-based analysis and bug fixes.")

# User Input
user_code = st.text_area("Enter your Python code:", height=250)

if st.button("Review Code"):
    if user_code.strip():
        with st.spinner("Analyzing your code..."):
            feedback = review_code(user_code)

        # Display AI feedback in a structured format
        st.subheader("📝 AI Code Review Report")
        st.markdown("**Issues Found:**")
        st.write(feedback)  # Modify this to extract structured data if possible

        st.markdown("**🔧 Suggested Fixes:**")
        # Assuming the AI provides fixed code, display it in a code block
        st.code(feedback, language="python")
    else:
        st.warning("⚠️ Please enter some Python code before submitting.")

st.markdown("---")
st.info("🚀 Powered by Google Gemini AI")

