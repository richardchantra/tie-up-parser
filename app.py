import streamlit as st
import base64

def display_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

st.set_page_config(layout="wide")
st.title("PDF Viewer with Tabs")

tab1, tab2 = st.tabs(["PDF 1", "PDF 2"])

with tab1:
    st.header("Viewing PDF 1")
    display_pdf("example1.pdf")  # Replace with your file path

with tab2:
    st.header("Viewing PDF 2")
    display_pdf("example2.pdf")  # Replace with your file path
