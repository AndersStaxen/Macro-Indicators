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
st.markdown("---")

# --- Code Snippets / Python Link ---
import base64

def get_python_download_link(file_path):
    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="Data_Visualization.py">Download Data Visualization.py</a>'
        return href

st.markdown(get_python_download_link('Data_Visualization.py'), unsafe_allow_html=True)


# --- Load Excel ---
@st.cache_data
def load_data():
    file = 'Economic_Indicators.xlsx'
    xls = pd.ExcelFile(file)
    return {sheet: xls.parse(sheet) for sheet in xls.sheet_names}

data_dict = load_data()

# --- Table View ---
st.subheader("All Macroeconomic Variables")

# Assuming data_dict is already defined with keys like "All Data", "Monthly", etc.
sheet_names = list(data_dict.keys())
default_index = sheet_names.index("Monthly") if "Monthly" in sheet_names else 0

sheet_name = st.selectbox("Choose a frequency", sheet_names, index=default_index)


# --- Code Snippets ---
st.subheader("💡 Sample Python Code for Analysis")
st.code("""
from statsmodels.api import OLS, add_constant
import matplotlib.pyplot as plt

# Example: Regression of GDP on Unemployment Rate
df = data_dict['Quarterly'].dropna()
X = add_constant(df['UNRATE'])
y = df['GDPC1']
model = OLS(y, X).fit()
print(model.summary())

# Plotting residuals
plt.scatter(model.fittedvalues, model.resid)
plt.title("Residuals Plot")
plt.show()
""", language='python')
