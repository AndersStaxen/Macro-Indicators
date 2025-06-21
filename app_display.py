# app.py

import streamlit as st
import pandas as pd
import base64

# --- Page Config ---
st.set_page_config(page_title="U.S. Macroeconomic Dashboard", layout="wide")

# --- Title & Description ---
st.title("🇺🇸 U.S. Macroeconomic Indicators")
st.markdown("""
This dashboard presents key U.S. macroeconomic indicators using data sourced from the Federal Reserve (FRED).
The project aims to centralize and visualize critical time-series data for economic analysis.

**Features:**
- 📈 Line chart of U.S. Real GDP
- 🧮 Table view of all available indicators
- 🧰 Reusable Python analysis methods
- 📁 Excel download of the full dataset
""")

# --- Load Excel ---
@st.cache_data
def load_data():
    file = 'Economic_Indicators.xlsx'
    xls = pd.ExcelFile(file)
    return {sheet: xls.parse(sheet) for sheet in xls.sheet_names}

data_dict = load_data()

# --- GDP Line Chart ---
if 'Quarterly' in data_dict:
    quarterly_df = data_dict['Quarterly']
    if 'GDPC1' in quarterly_df.columns:
        st.subheader("📉 Real U.S. GDP (GDPC1)")
        gdp_series = quarterly_df[['DATE', 'GDPC1']].dropna()
        gdp_series['DATE'] = pd.to_datetime(gdp_series['DATE'])
        gdp_series.set_index('DATE', inplace=True)
        st.line_chart(gdp_series)
    else:
        st.warning("Real GDP (GDPC1) not found in Quarterly data.")
else:
    st.error("Quarterly sheet not found in Excel file.")

# --- Table View ---
st.subheader("📊 All Macroeconomic Variables")
sheet_name = st.selectbox("Choose a frequency", list(data_dict.keys()))
st.dataframe(data_dict[sheet_name], use_container_width=True)

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

# --- Download Excel ---
def get_excel_download_link(file_path):
    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="Economic_Indicators.xlsx">📥 Download Excel File</a>'
        return href

st.markdown("---")
st.markdown(get_excel_download_link('Economic_Indicators.xlsx'), unsafe_allow_html=True)
