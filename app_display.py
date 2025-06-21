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

# Or, a simpler text link:
# st.sidebar.markdown("[My LinkedIn Profile](YOUR_LINKEDIN_URL_HERE)")
# st.sidebar.markdown("[My GitHub Profile](YOUR_GITHUB_URL_HERE)")


# --- Page Config ---
st.set_page_config(page_title="U.S. Macroeconomic Dashboard", layout="wide")

# --- Title & Description ---
st.title("U.S. Macroeconomic Indicators")
st.markdown("""
This dashboard presents key U.S. macroeconomic indicators using data sourced from the Federal Reserve (FRED).
The project aims to centralize critical time-series data for economic analysis.
Additionally, links to download the full dataset in Excel format and view more comprehensive ways of using Python to analyze the data are provided.
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
    'CPI MoM % Change',
    'CPI YoY % Change',
    'Core CPI MoM % Change',
    'Core CPI YoY % Change',
    'PCE MoM % Change',
    'PCE YoY % Change',
    'Core PCE MoM % Change',
    'Core PCE YoY % Change'
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


# Assuming data_dict is loaded and contains your dataframes by frequency
# and indicators dictionary is available

# Add this section somewhere in your main app.py, perhaps after "All Macroeconomic Variables" table

st.subheader("Interactive Time Series Visualizations")

# Get a list of all variable names for selection
# You might want to filter this list based on data availability
available_plot_variables = [name for name, details in indicators.items()] + derived_indicators

selected_plot_variables = st.multiselect(
    "Select variables to visualize",
    options=available_plot_variables,
    default=['Real GDP', 'CPI'] # Example defaults
)

if selected_plot_variables:
    # Determine the most appropriate frequency for plotting.
    # This is a simplification; a more robust solution might handle mixed frequencies.
    # For now, let's assume we plot from the "Monthly" sheet if available, otherwise "All Data"
    plot_frequency_sheet = "Monthly" if "Monthly" in data_dict else list(data_dict.keys())[0]

    if plot_frequency_sheet in data_dict:
        df_plot = data_dict[plot_frequency_sheet].set_index('Date') # Assuming a 'Date' column

        # Filter the DataFrame to only include selected columns.
        # You'll need to map variable names back to FRED codes if your DF columns are codes.
        # If your DF columns are already clean names, this is simpler.
        # For simplicity, let's assume 'Real GDP' and 'CPI' are directly columns in your DF
        columns_to_plot = []
        for var_name in selected_plot_variables:
            # This mapping needs to be precise. If your DF columns are FRED codes,
            # you'd need to find the FRED code from 'indicators' dict.
            # If your DF columns are the full variable names, you can use them directly.
            if var_name in df_plot.columns: # Check if the column exists
                columns_to_plot.append(var_name)
            elif var_name in indicators and indicators[var_name]['code'] in df_plot.columns:
                columns_to_plot.append(indicators[var_name]['code'])
            # Handle derived variables separately if their names aren't direct columns
            # For now, this example assumes direct column names or FRED codes in DF.

        if columns_to_plot:
            import plotly.express as px
            # Ensure the data is numeric for plotting
            df_for_chart = df_plot[columns_to_plot].apply(pd.to_numeric, errors='coerce')

            fig = px.line(df_for_chart,
                          x=df_for_chart.index,
                          y=columns_to_plot,
                          title='Selected Macroeconomic Indicators Over Time')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Selected variables not found in the chosen data frequency.")
    else:
        st.info("No data available for plotting. Please ensure your Excel file contains a 'Monthly' sheet or adjust the data loading.")
else:
    st.info("Select variables from the dropdown above to see their time series.")


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
