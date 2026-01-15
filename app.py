import streamlit as st

st.set_page_config(page_title="AI Data Detective", layout="wide")

st.title("🕵️ AI Data Detective")
st.write("If you can see this, Streamlit is working.")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")
