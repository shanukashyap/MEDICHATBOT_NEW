import streamlit as st

def pdf_uploader():
    st.title("PDF Uploder")
    uploaded_file = st.file_uploader("choose a PDF file", type="pdf",accept_multiple_files=True,)
    if uploaded_file is not None:
        st.success("File uploaded successfully")
    return uploaded_file
