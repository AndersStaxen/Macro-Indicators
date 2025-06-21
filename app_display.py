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
- 📁 Excel download of the full dataset
- 🧰 Reusable Python analysis file
""")

# --- Download Excel ---
def get_excel_download_link(file_path):
    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="Economic_Indicators.xlsx">Download Excel File</a>'
        return href
st.markdown(get_excel_download_link('Economic_Indicators.xlsx'), unsafe_allow_html=True)

# --- Code Snippets / Python Link ---
import base64

def get_python_download_link(file_path):
    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="Data_Visualization.py">Download Data Visualization.py</a>'
        return href
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

