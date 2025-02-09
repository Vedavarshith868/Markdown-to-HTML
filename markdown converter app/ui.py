import streamlit as st
import requests

st.set_page_config(page_title="Markdown to HTML Converter", layout="wide")

st.title("📄 Markdown to HTML Converter")
st.markdown("Upload a Markdown (.md) file to convert it into formatted HTML.")

uploaded_file = st.file_uploader("Choose a Markdown file", type=["md"])

if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    response = requests.post("http://127.0.0.1:5000/upload", files=files) #connecting line
    
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