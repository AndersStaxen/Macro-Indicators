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
        # Adjusted text for the link
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="Economic_Indicators.py">Download Entire Python Notebook Script</a>'
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
col1_python, col2_python = st.columns([0.8, 0.2]) # Adjust ratios as needed
with col1_python:
    st.markdown("- 📑 Reusable Python Notebook")
with col2_python:
    st.markdown(get_python_notebook_download_link('Economic_Indicators.py'), unsafe_allow_html=True)

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

# NEW: Selectbox for choosing the data frequency for the plot
# You can customize these options based on which sheets you want to allow for plotting.
# It's good to include "All Data" as an option too, as it covers everything.
plot_frequency_options = ["All Data", "Monthly", "Quarterly", "Daily", "Weekly"] # Order as desired

# Filter to only include sheets that actually exist in your data_dict
existing_plot_frequencies = [
    freq for freq in plot_frequency_options if freq in data_dict
]

if not existing_plot_frequencies:
    st.error("No data sheets available for time series visualization. Please ensure your Excel file is loaded correctly.")
    st.stop() # Stop execution if no data is found for plotting

# Set a default selection for the plot frequency
default_plot_freq_index = 0
if "Monthly" in existing_plot_frequencies:
    default_plot_freq_index = existing_plot_frequencies.index("Monthly")
elif "All Data" in existing_plot_frequencies: # Fallback to All Data if Monthly isn't there
    default_plot_freq_index = existing_plot_frequencies.index("All Data")


available_plot_frequencies = [freq for freq in existing_plot_frequencies if freq != 'All Data']


selected_plot_frequency = st.selectbox(
    "Select data frequency for visualization:",
    options=available_plot_frequencies,
    index=default_plot_freq_index,
    key="plot_freq_selector"
)

if selected_plot_frequency in indicators:
    available_plot_variables = list(indicators[selected_plot_frequency].keys()) + derived_indicators
else:
    available_plot_variables = derived_indicators  # Fallback if no indicators found for that frequency


selected_plot_variables = st.multiselect(
    "Select variables to visualize",
    options=available_plot_variables,
    default=[], # Keep it empty or add some relevant defaults
    key="variable_selector"
)

if selected_plot_variables:
    if plot_data_sheet in data_dict:
        df_plot = data_dict[plot_data_sheet].copy()

        # Ensure 'Date' column is present and is a datetime object, then set as index
        if 'Date' in df_plot.columns:
            df_plot['Date'] = pd.to_datetime(df_plot['Date'], errors='coerce')
            df_plot = df_plot.set_index('Date').sort_index()
        else:
            st.error(f"'{plot_data_sheet}' sheet does not contain a 'Date' column. Cannot plot.")
            st.stop()

        # --- Debugging Tip 1: Print all actual columns in the DataFrame ---
        # st.info(f"Columns found in '{plot_data_sheet}' sheet: {df_plot.columns.tolist()}")

        columns_to_plot = []
        display_names = {}
        actual_df_columns_lower = [col.lower().strip() for col in df_plot.columns]

        for var_name in selected_plot_variables:
            found_column = None
            display_for_plot = var_name

            # 1. Try to match by FRED Code (for primary indicators)
            if var_name in indicators:
                fred_code = indicators[var_name]['code']

                if fred_code in df_plot.columns:
                    found_column = fred_code
                    display_for_plot = var_name
                elif var_name in df_plot.columns:
                    found_column = var_name
                    display_for_plot = var_name
                else:
                    try_fred_code_lower = fred_code.lower().strip()
                    try_var_name_lower = var_name.lower().strip()

                    if try_fred_code_lower in actual_df_columns_lower:
                        found_column = df_plot.columns[actual_df_columns_lower.index(try_fred_code_lower)]
                        display_for_plot = var_name
                    elif try_var_name_lower in actual_df_columns_lower:
                        found_column = df_plot.columns[actual_df_columns_lower.index(try_var_name_lower)]
                        display_for_plot = var_name

            # 2. Try to match by the variable name itself (for derived indicators or if primary indicators are named directly)
            elif var_name in df_plot.columns:
                found_column = var_name
                display_for_plot = var_name
            else: # Fallback for derived variables, check case-insensitive and stripped
                try_var_name_lower = var_name.lower().strip()
                if try_var_name_lower in actual_df_columns_lower:
                    found_column = df_plot.columns[actual_df_columns_lower.index(try_var_name_lower)]
                    display_for_plot = var_name

            if found_column:
                columns_to_plot.append(found_column)
                display_names[found_column] = display_for_plot
            else:
                st.warning(f"Data for '{var_name}' not found in the '{plot_data_sheet}' sheet. Please ensure the column name is correct in your Excel file for this frequency.")

        # --- Debugging Tip 2: Print the columns that were actually identified for plotting ---
        # st.info(f"Identified columns for plotting: {columns_to_plot}")
        # st.info(f"Display name mapping: {display_names}")


        if columns_to_plot:
            import plotly.express as px

            # Select and rename columns
            df_for_chart = df_plot[columns_to_plot].rename(columns=display_names)

            # Ensure numeric type, converting non-numeric to NaN
            df_for_chart = df_for_chart.apply(pd.to_numeric, errors='coerce')

            # Check for columns that are entirely NaN after conversion
            valid_columns_for_plotting = []
            for col_name in df_for_chart.columns:
                if df_for_chart[col_name].dropna().empty:
                    st.warning(f"'{col_name}' has no valid numeric data points in the '{plot_data_sheet}' sheet and will not be plotted.")
                else:
                    valid_columns_for_plotting.append(col_name)

            if not valid_columns_for_plotting:
                st.info("No selected variables have valid numeric data points to plot in the chosen frequency.")
                # This 'return' might be too aggressive if you want to show an empty plot.

            # Filter df_for_chart to only include columns with valid data
            df_for_chart = df_for_chart[valid_columns_for_plotting]


            fig = px.line(df_for_chart,
                          x=df_for_chart.index,
                          y=df_for_chart.columns,
                          title=f'Selected Macroeconomic Indicators ({plot_data_sheet} Data) Over Time',
                          labels={'value': 'Value', 'index': 'Date'})

            fig.update_xaxes(
                rangeslider_visible=True,
                rangeselector=dict(
                    buttons=list([
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(step="all")
                    ])
                )
            )
            fig.update_layout(hovermode="x unified")

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No valid variables selected or found in the data for plotting.")
    else:
        st.error(f"The selected sheet '{plot_data_sheet}' was not found in your Excel file. Please select an existing sheet.")
else:
    st.info("Select data frequency and variables from the dropdowns above to see their time series.")
