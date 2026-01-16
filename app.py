import streamlit as st
import pandas as pd

from insights.eda import run_eda
from insights.anomaly import detect_anomalies

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="AI Data Detective",
    layout="wide"
)

st.title("AI Data Detective")
st.caption("Upload your data. Discover insights. Ask questions.")

st.divider()

# -------------------------------------------------
# File upload
# -------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is None:
    st.info("Upload a CSV file to begin")
    st.stop()

# -------------------------------------------------
# Load data
# -------------------------------------------------
try:
    df = pd.read_csv(uploaded_file)
except Exception as e:
    st.error(f"Error reading file: {e}")
    st.stop()

st.success("File uploaded successfully")

# -------------------------------------------------
# Data preview
# -------------------------------------------------
st.subheader("Data Preview")
st.dataframe(df.head(50), use_container_width=True)

# -------------------------------------------------
# Dataset intelligence (STEP 8)
# -------------------------------------------------
st.divider()
st.subheader("Automatic Dataset Intelligence")

eda_summary = run_eda(df)
anomalies = detect_anomalies(df)

col1, col2 = st.columns(2)

with col1:
    st.markdown("Missing Values (Top Columns)")
    if "missing_values" in eda_summary:
        st.write(dict(list(eda_summary["missing_values"].items())[:5]))
    else:
        st.write("No missing value analysis available")

with col2:
    st.markdown("Detected Anomalies")
    if anomalies:
        st.write(anomalies)
    else:
        st.write("No significant anomalies detected")

# -------------------------------------------------
# Dataset summary
# -------------------------------------------------
st.divider()
st.subheader("Dataset Summary")

c1, c2, c3 = st.columns(3)
c1.metric("Rows", df.shape[0])
c2.metric("Columns", df.shape[1])
c3.metric("Missing Values", df.isna().sum().sum())

with st.expander("View column details"):
    st.write(df.dtypes)

# -------------------------------------------------
# Natural language input (STEP 9 → STEP 10)
# -------------------------------------------------
st.divider()
st.subheader("Ask a question about your data")

user_query = st.text_input(
    "Example: Show correlations, Find outliers, Plot trends over time"
)

if not user_query:
    st.info("Type a question to generate insights or visualizations")
    st.stop()

# -------------------------------------------------
# Placeholder for intent → visualization (STEP 10.2)
# -------------------------------------------------
st.write("You asked:")
st.write(user_query)

st.info("Intent parsing and visualization coming next")
