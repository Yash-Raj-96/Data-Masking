import streamlit as st
import pandas as pd
from masking import mask_column
from utils import load_csv, save_masked_data

st.title("🔐 Simple Data Masking Tool for Privacy-Preserving Analytics")

uploaded_file = st.file_uploader("Upload CSV File", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("### Original Data Sample:", data.head())
    
    st.write("### Select Columns to Mask")
    columns = data.columns.tolist()
    column_to_mask = st.selectbox("Select column", columns)
    mask_type = st.selectbox("Select mask type", ['random_string', 'email', 'phone', 'name'])

    if st.button("Apply Mask"):
        masked_data = mask_column(data.copy(), column_to_mask, mask_type)
        st.write("### Masked Data Sample:", masked_data.head())

        if st.button("Save Masked Data"):
            output_path = save_masked_data(masked_data, 'masked_data', 'masked_output.csv')
            st.success(f"Masked data saved at: {output_path}")

st.sidebar.info("Upload a CSV file, select column, choose mask type, mask and download!")
