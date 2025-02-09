import streamlit as st
import requests, os

st.set_page_config(page_title="Markdown to HTML Converter", layout="wide")

st.title("📄 Markdown to HTML Converter")
st.markdown("Upload a Markdown (.md) file to convert it into formatted HTML.")

uploaded_file = st.file_uploader("Choose a Markdown file", type=["md"])

if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    #response = requests.post("https://markdown-to-html-1.onrender.com", files=files) #connecting line

    API_URL = os.getenv("API_URL")  # Get API URL from environment variable

    if API_URL is None:
        st.error("API_URL is not set. Please configure environment variables.")
    else:
        response = requests.post(f"{API_URL}/upload", files=files)
    
        if response.status_code == 200:
            html_content = response.json().get("html", "")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📝 Converted HTML Code")
                st.code(html_content, language="html")
            
            with col2:
                st.subheader("📌 HTML Preview")
                st.markdown(html_content, unsafe_allow_html=True)
        else:
            st.error("Failed to convert the file. Please try again.")
