import streamlit as st
import os

st.set_page_config(layout="wide")
st.title("PDF Viewer with Tabs")

uploaded_files = st.file_uploader("Upload two PDFs", type="pdf", accept_multiple_files=True)

if uploaded_files and len(uploaded_files) == 2:
    tabs = st.tabs(["PDF 1", "PDF 2"])
    for i in range(2):
        with open(f"temp_{i}.pdf", "wb") as f:
            f.write(uploaded_files[i].read())
        with tabs[i]:
            st.markdown(f"#### Viewing PDF {i+1}")
            st.markdown(
                f'<iframe src="https://docs.google.com/gview?url=https://yourdomain.com/path/to/temp_{i}.pdf&embedded=true" '
                f'width="100%" height="800px" frameborder="0"></iframe>',
                unsafe_allow_html=True
            )
else:
    st.info("Please upload exactly two PDFs.")
