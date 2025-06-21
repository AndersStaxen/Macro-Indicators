# app.py

import streamlit as st
import pandas as pd
import base64

# --- Page Config ---
st.set_page_config(page_title="U.S. Macroeconomic Dashboard", layout="wide")

# --- Title & Description ---
st.title("U.S. Macroeconomic Indicators")
st.markdown("""
This dashboard presents key U.S. macroeconomic indicators using data sourced from the Federal Reserve (FRED).
The project aims to centralize critical time-series data for economic analysis. 
Additionally, links to download the full dataset in Excel format and view more comprehensive ways of using Python to analyze the data are provided.

**Features:**
- 🧮 Table view of all available indicators
import streamlit as st
import pandas as pd
import base64

# --- Load Excel ---
@st.cache_data
def load_data():
    file = 'Economic_Indicators.xlsx'
    xls = pd.ExcelFile(file)
    return {sheet: xls.parse(sheet) for sheet in xls.sheet_names}

data_dict = load_data()

# --- Table View (from previous answer) ---
st.subheader("All Macroeconomic Variables")
sheet_options = list(data_dict.keys())
try:
    default_index = sheet_options.index("Monthly")
except ValueError:
    default_index = 0
sheet_name = st.selectbox(
    "Choose a frequency",
    options=sheet_options,
    index=default_index
)
st.dataframe(data_dict[sheet_name], use_container_width=True)


# --- Download Excel Function ---
def get_excel_download_link(file_path):
    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        # Adjusted text for the link to be more concise since the explanation is separate
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="Economic_Indicators.xlsx">Download</a>'
        return href

# --- Download Python File Function ---
def get_python_download_link(file_path):
    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        # Adjusted text for the link
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="Data_Visualization.py">Download</a>'
        return href

st.subheader("Download Options")

# --- Excel Download Row ---
col1_excel, col2_excel = st.columns([0.8, 0.2]) # Adjust ratios as needed

with col1_excel:
    st.markdown("- 📁 Excel download of the full dataset")

with col2_excel:
    st.markdown(get_excel_download_link('Economic_Indicators.xlsx'), unsafe_allow_html=True)

# --- Python Analysis File Download Row ---
col1_python, col2_python = st.columns([0.8, 0.2]) # Adjust ratios as needed

with col1_python:
    st.markdown("- 🧰 Reusable Python analysis file")

with col2_python:
    st.markdown(get_python_download_link('Data_Visualization.py'), unsafe_allow_html=True)

st.markdown("---")

import streamlit as st
import pandas as pd

# --- Load Excel ---
@st.cache_data
def load_data():
    file = 'Economic_Indicators.xlsx'
    xls = pd.ExcelFile(file)
    return {sheet: xls.parse(sheet) for sheet in xls.sheet_names}

data_dict = load_data()

# --- Table View ---
st.subheader("All Macroeconomic Variables")

# Get the list of sheet names (options for the selectbox)
sheet_options = list(data_dict.keys())

# Determine the index of "Monthly" in the list of options
# Use .index() to find the position. Add error handling in case "Monthly" isn't found.
try:
    default_index = sheet_options.index("Monthly")
except ValueError:
    default_index = 0  # Fallback to the first option if "Monthly" isn't found

# Create the selectbox with the default index set
sheet_name = st.selectbox(
    "Choose a frequency",
    options=sheet_options,
    index=default_index  # This sets the default selected option
)

# Display the dataframe for the selected sheet
st.dataframe(data_dict[sheet_name], use_container_width=True)

