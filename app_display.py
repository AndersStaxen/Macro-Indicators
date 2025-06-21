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
- 🧮 Table view of all available indicators
- 📁 Excel download of the full dataset
- 🧰 Reusable Python analysis methods
""")

# --- Load Excel ---
@st.cache_data
def load_data():
    file = 'Economic_Indicators.xlsx'
    xls = pd.ExcelFile(file)
    return {sheet: xls.parse(sheet) for sheet in xls.sheet_names}

data_dict = load_data()

# --- Table View ---
st.subheader("📊 All Macroeconomic Variables")
sheet_name = st.selectbox("Choose a frequency", list(data_dict.keys()))

# --- Download Excel ---
def get_excel_download_link(file_path):
    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="Economic_Indicators.xlsx">📥 Download Excel File</a>'
        return href

st.markdown("---")
st.markdown(get_excel_download_link('Economic_Indicators.xlsx'), unsafe_allow_html=True)


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

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Load your processed data
@st.cache_data

def load_data():
    file_path = "Economic_Indicators.xlsx"
    xls = pd.ExcelFile(file_path)
    monthly_df = pd.read_excel(xls, 'Monthly', parse_dates=['Date'])
    return monthly_df

# Utility function to plot a series
def _plot_series(ax, df, col, label, color_index):
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
    if col in df:
        ax.plot(df['Date'], df[col], label=label, color=colors[color_index], linewidth=2)

# Load data
monthly_df = load_data()
monthly_df['Date'] = pd.to_datetime(monthly_df['Date'])

# Define filtered dataset for plotting
plot_df = monthly_df[(monthly_df['Date'] >= '2016-01-01') & (monthly_df['Date'] <= '2024-12-31')].copy()
plot_df.sort_values('Date', inplace=True)

# --- Streamlit App ---
st.set_page_config(page_title="Economic Dashboard", layout="wide")
st.title("📊 Economic Indicator Dashboard")

# Tabs for different visualizations
tabs = st.tabs(["Inflation % Change", "Placeholder Tab 2", "Placeholder Tab 3"])

# --- Tab 1: Inflation ---
with tabs[0]:
    st.subheader("Inflation: MoM and YoY % Change")
    fig, ax = plt.subplots(figsize=(10, 5))

    _plot_series(ax, plot_df, 'CPI MoM %', 'CPI MoM', 0)
    _plot_series(ax, plot_df, 'CPI YoY %', 'CPI YoY', 1)
    _plot_series(ax, plot_df, 'PCE MoM %', 'PCE MoM', 2)
    _plot_series(ax, plot_df, 'PCE YoY %', 'PCE YoY', 3)

    ax.set_title('Inflation Rates: MoM and YoY')
    ax.set_ylabel('% Change')
    ax.set_xlabel('Year')
    ax.legend()
    ax.yaxis.set_major_formatter(PercentFormatter())

    st.pyplot(fig)

# --- Tab 2 & 3: Placeholder ---
with tabs[1]:
    st.subheader("More visualizations coming soon")
    st.info("This section is under development.")

with tabs[2]:
    st.subheader("More visualizations coming soon")
    st.info("This section is under development.")
