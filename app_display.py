# app.py

import streamlit as st
import pandas as pd
import base64

# app.py (add this snippet)

# --- About Me / Contact (in sidebar) ---
st.sidebar.subheader("About the Author")
st.sidebar.markdown(
    """
Anders Staxen is a graduate student at Columbia University, specializing in international finance and quantitative analysis.
He holds a bachelor’s degree in finance and political science, with previous experience in wealth management and international political economy research.
    Connect with me on LinkedIn
    """
)
st.sidebar.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/andersstaxen/)")

st.sidebar.markdown("---") # Separator
st.sidebar.subheader("Related Research")

st.sidebar.markdown(
    """
Sovereign 10-Year Yield Predictor; Using 2010-2019 panel data with country fixed effects, I investigated the institutional and macroeconomic determinants of countries' 10-year yield.
Key findings show that Real GDP Growth (coefficient: -0.2426) and Inflation (coefficient: 0.1932) are statistically significant predictors of sovereign yields.
    """
)

st.sidebar.markdown("[Explore Claude Artifact](https://claude.ai/public/artifacts/7ed39c45-a853-4338-92c9-f8eb933cf8f8)")


# --- Page Config ---
st.set_page_config(page_title="U.S. Macroeconomic Dashboard", layout="wide")

# --- Title & Description ---
st.title("U.S. Macroeconomic Indicators")
st.markdown("""
This dashboard presents 49 key U.S. macroeconomic indicators using data sourced from the Federal Reserve (FRED).
Currently, the data displayed covers the period from January 1, 2017, to December 31, 2024; however, this time period can be customized when running the Python script locally.
The project aims to centralize critical time-series data for economic analysis.
Additionally, links to download the full dataset in Excel and view more comprehensive ways of using Python to analyze the data are provided.
""")

# --- Features List & Download Links (Merged and Improved) ---
st.markdown("**Features:**")

# --- Download Excel Function ---
def get_excel_download_link(file_path):
    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        # Adjusted text for the link to be more concise since the explanation is separate
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="Economic_Indicators.xlsx">Download Excel File</a>'
        return href

# --- Download Python File Function ---
def get_python_download_link(file_path):
    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        # Adjusted text for the link
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="Data_Visualization.py">Download Python Analysis Script</a>'
        return href

# --- Download Python Notebook Function ---
def get_python_notebook_download_link(file_path):
    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="economic_indicators.py">Download Entire Python Notebook Script</a>'
        return href

# Feature 1: Table View (already present, just adding bullet point)
st.markdown("- 🧮 Table view of all available indicators") # Kept as is

# Feature 2: Excel Download
col1_excel, col2_excel = st.columns([0.8, 0.2]) # Adjust ratios as needed
with col1_excel:
    st.markdown("- 📁 Excel download of the full dataset")
with col2_excel:
    st.markdown(get_excel_download_link('Economic_Indicators.xlsx'), unsafe_allow_html=True)

# Feature 3: Reusable Python File
col1_python, col2_python = st.columns([0.8, 0.2]) # Adjust ratios as needed
with col1_python:
    st.markdown("- 🧰 Reusable Python analysis file")
with col2_python:
    st.markdown(get_python_download_link('Data_Visualization.py'), unsafe_allow_html=True)

# Feature 4: Entire Python Notebook
col1_notebook, col2_notebook = st.columns([0.8, 0.2])
with col1_notebook:
    st.markdown("- 📑 Entire Python Notebook")
with col2_notebook:
    st.markdown(get_python_notebook_download_link('economic_indicators.py'), unsafe_allow_html=True)


st.markdown("---") # Separator


# --- Load Excel ---
@st.cache_data
def load_data():
    try:
        file = 'Economic_Indicators.xlsx'
        xls = pd.ExcelFile(file)
        return {sheet: xls.parse(sheet) for sheet in xls.sheet_names}
    except FileNotFoundError:
        st.warning("Economic_Indicators.xlsx not found. Please ensure the file is in the correct directory.")
        return {} # Return an empty dict if file is not found

data_dict = load_data()

# --- Indicators Dictionary (moved here for better organization) ---
indicators = {
    # --- Real Economy ---
    'Real GDP': {'code': 'GDPC1', 'frequency': 'quarterly'},
    'Nominal GDP': {'code': 'GDP', 'frequency': 'quarterly'},
    'GNP': {'code': 'GNPCA', 'frequency': 'quarterly'},
    'Retail Sales': {'code': 'MRTSSM44000USS', 'frequency': 'monthly'},
    'Unemployment Rate': {'code': 'UNRATE', 'frequency': 'monthly'},
    'Labor Force Participation': {'code': 'CIVPART', 'frequency': 'monthly'},
    'Employment Level': {'code': 'PAYEMS', 'frequency': 'monthly'},

    # --- Inflation & Prices ---
    'PCE': {'code': 'PCEPI', 'frequency': 'monthly'},
    'Core PCE': {'code': 'PCEPILFE', 'frequency': 'monthly'},
    'CPI': {'code': 'CPIAUCSL', 'frequency': 'monthly'},
    'Core CPI': {'code': 'CPILFESL', 'frequency': 'monthly'},
    'M2 Money Stock': {'code': 'M2', 'frequency': 'weekly'},
    'M2 Money Stock Growth': {'code': 'M2REAL', 'frequency': 'monthly'},
    'Average Hourly Wages': {'code': 'CES0500000003', 'frequency': 'monthly'},

    # --- Production ---
    'Industrial Production': {'code': 'INDPRO', 'frequency': 'monthly'},
    'Capacity Utilization': {'code': 'TCU', 'frequency': 'monthly'},
    'Durable Goods Orders': {'code': 'DGORDER', 'frequency': 'monthly'},
    'Producer Price Index': {'code': 'PPIACO', 'frequency': 'monthly'},

    # --- Interest Rates & Credit ---
    'Federal Funds Rate': {'code': 'FEDFUNDS', 'frequency': 'monthly'},
    '2-Year Treasury Constant Maturity Rate': {'code': 'DGS2', 'frequency': 'daily'},
    '5-Year Treasury Constant Maturity Rate': {'code': 'DGS5', 'frequency': 'daily'},
    '10-Year Treasury Yield': {'code': 'DGS10', 'frequency': 'daily'},
    '30-Year Treasury Yield': {'code': 'DGS30', 'frequency': 'daily'},
    '30-Year Fixed Rate Mortgage Average': {'code': 'MORTGAGE30US', 'frequency': 'weekly'},
    'Aaa Corporate Bond Spread': {'code': 'AAAFF', 'frequency': 'daily'},
    'Baa Corporate Bond Spread': {'code': 'BAAFF', 'frequency': 'daily'},

    # --- Debt & Household Indicators ---
    'Total Public Debt': {'code': 'GFDEBTN', 'frequency': 'quarterly'},
    'Total Public Debt as % of GDP': {'code': 'GFDEGDQ188S', 'frequency': 'quarterly'},
    'Household Debt Service Payments as % of Disposable Personal Income': {'code': 'TDSP', 'frequency': 'quarterly'},
    'Household Debt-to-GDP': {'code': 'HDTGPDUSQ163N', 'frequency': 'quarterly'},
    'Federal Debt Held by Foreign Investors': {'code': 'FDHBFIN', 'frequency': 'quarterly'},
    'Delinquency Rate on Credit Card Loans': {'code': 'DRCCLACBS', 'frequency': 'quarterly'},
    'Delinquency Rate on Mortgages': {'code': 'DRSFRMACBS', 'frequency': 'quarterly'},

    # --- Financial Markets & Expectations ---
    'Consumer Sentiment': {'code': 'UMCSENT', 'frequency': 'monthly'},
    'VIX Volatility Index': {'code': 'VIXCLS', 'frequency': 'daily'},
    'S&P 500': {'code': 'SP500', 'frequency': 'daily'},
    'Home Sales': {'code': 'EXHOSLUSM495S', 'frequency': 'monthly'},
}

# --- Additional derived indicators ---
derived_indicators = [
    'CPI MoM %',
    'CPI YoY %',
    'Core CPI MoM %',
    'Core CPI YoY %',
    'PCE MoM %',
    'PCE YoY %',
    'Core PCE MoM %',
    'Core PCE YoY %'
]


# --- Table View (Existing, with "Monthly" default) ---
if data_dict: # Only show this if data was loaded successfully
    st.subheader("All Macroeconomic Variables")
    sheet_options = list(data_dict.keys())
    try:
        default_index = sheet_options.index("Monthly")
    except ValueError:
        default_index = 0
    sheet_name = st.selectbox(
        "Choose a frequency for data table",
        options=sheet_options,
        index=default_index
    )
    st.dataframe(data_dict[sheet_name], use_container_width=True)


# --- Show List of Variables (New Section) ---
st.subheader("Available Macroeconomic Variables")

with st.expander("Click to see the full list of variables"):
    # Prepare data for DataFrame
    variable_list_data = []
    for name, details in indicators.items():
        variable_list_data.append({"Variable Name": name, "FRED Code": details['code'], "Frequency": details['frequency'].capitalize()})

    # Add derived indicators
    for name in derived_indicators:
        variable_list_data.append({"Variable Name": name, "FRED Code": "N/A (Derived)", "Frequency": "Calculated"})

    df_variables = pd.DataFrame(variable_list_data)
    st.dataframe(df_variables, use_container_width=True, hide_index=True)


# --- Time Series Visualization ---

# app.py (Modify your "Interactive Time Series Visualizations" section with this)

st.subheader("Interactive Time Series Visualizations")

# --- User-selected frequency ---
selected_frequency = st.selectbox("Select Data Frequency", ['daily', 'weekly', 'monthly', 'quarterly'])

# --- Filter indicators by selected frequency ---
available_variables = [
    name for name, meta in indicators.items() if meta['frequency'] == selected_frequency
]

# --- Optional: Add derived indicators separately (if needed for certain frequencies) ---
if selected_frequency == 'monthly':
    available_variables += derived_indicators

# --- User selects variable ---
selected_indicators = st.multiselect("Select Variables", available_variables)

# --- Get the correct dataframe ---
df = data_dict.get(selected_frequency)

if df is not None and not df.empty:
    import matplotlib.pyplot as plt
    plt.style.use('seaborn-v0_8-darkgrid')

    fig, ax = plt.subplots(figsize=(12, 6))

    found_any = False
    for indicator in selected_indicators:
        if indicator in df.columns:
            df_plot = df[['Date', indicator]].dropna()
            ax.plot(df_plot['Date'], df_plot[indicator], label=indicator)
            found_any = True
        else:
            st.warning(f"'{indicator}' not found in {selected_frequency} data columns.")

    if found_any:
        ax.set_xlabel('Date')
        ax.set_ylabel('Value')
        ax.set_title(f'Time Series of Selected Indicators ({selected_frequency} Data)')
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)
    else:
        st.warning("No valid indicators selected for plotting.")
else:
    st.error(f"No data loaded for {selected_frequency}. Check your data loading function or Excel sheets.")
