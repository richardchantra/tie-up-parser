import streamlit as st
import pdfplumber
from io import BytesIO

st.title("PDF Viewer with Tabs")
uploaded_files = st.file_uploader("Upload two PDFs", type="pdf", accept_multiple_files=True)

if uploaded_files and len(uploaded_files) == 2:
    tabs = st.tabs(["PDF 1", "PDF 2"])
    
    for i in range(2):
        file = uploaded_files[i]
        with tabs[i]:
            st.subheader(f"Viewing: {file.name}")

            # Preview text using pdfplumber
            with pdfplumber.open(BytesIO(file.read())) as pdf:
                first_page = pdf.pages[0]
                st.text(first_page.extract_text())

            # Download option
            st.download_button(
                label=f"Download {file.name}",
                data=file,
                file_name=file.name,
                mime="application/pdf"
            )
else:
    st.info("Please upload exactly two PDF files.")
