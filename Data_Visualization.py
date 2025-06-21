"""# **Data Visualization**
---

### *Steps prior to perform data visualization*
"""

print(merged_df.columns.tolist())

# Define plot series function (if not already defined globally)
def _plot_series(ax, df, series_column, series_name=None, series_index=0):
    palette = list(sns.color_palette('Dark2'))
    xs = df['Date']
    ys = df[series_column]
    label = series_name if series_name else series_column
    ax.plot(xs, ys, label=label, color=palette[series_index % len(palette)])

# Filter the merged_df by date range
filtered_df = merged_df[(merged_df['Date'] >= start_date) & (merged_df['Date'] <= end_date)].copy()
# Use .copy() to avoid SettingWithCopyWarning in future operations
###--------------------------------------------------------------

"""---
### Simple Graphs
Using Unemployment Rate S&P 500
"""

# Unemployment Rate

test_dates = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')
]
print(test_dates[['Date', 'Unemployment Rate']].dropna().tail())

# Unemployment Rate (Simple Plot)

# Filter to the desired date range
test_dates = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')
]

# Clean data for plotting (remove NaNs)
test_clean = test_dates.dropna(subset=['Unemployment Rate'])

# Define plot series function (if not already defined globally)
# Note: If _plot_series is defined in a previous cell, this section is redundant.
def _plot_series(ax, df, series_column, series_name=None, series_index=0):
    palette = list(sns.color_palette('Dark2'))
    xs = df['Date']
    ys = df[series_column]
    label = series_name if series_name else series_column
    ax.plot(xs, ys, label=label, color=palette[series_index % len(palette)])

# Setup the plot
fig, ax = plt.subplots(figsize=(10, 5))

# Plot the series
_plot_series(ax, test_clean, 'Unemployment Rate', series_index=0)

# Set title and labels
ax.set_title('Unemployment Rate (2017–2024)')
ax.set_ylabel('Percent')
ax.set_xlabel('Date')
ax.legend()

# Show the plot
plt.show()

# S&P 500

test_dates = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')
]
print(test_dates[['Date', 'S&P 500']].dropna().tail())

# S&P 500 (Simple Plot)

# Filter to the desired date range
test_dates = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')
]

# Setup the plot
fig, ax = plt.subplots(figsize=(10, 5))

# Plot the series
_plot_series(ax, test_dates, 'S&P 500', series_index=0)

# Set title and labels
ax.set_title('S&P 500 (2017–2024)')
# Note: xlabel and ylabel were missing in the original snippet, added for completeness
ax.set_xlabel('Date')
ax.set_ylabel('Index')

# Show the plot
plt.show()

# Unemployment Rate and S&P 500 (Dual Axis Plot)

# Filter to the desired date range and clean data for Unemployment Rate
# Filter the overall data to the specific range for plotting
test_dates = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')
]

# Clean the Unemployment Rate data specifically for plotting (remove NaNs)
test_clean = test_dates.dropna(subset=['Unemployment Rate'])

# Create the dual-axis plot and setup the figure and the primary axis
fig, ax1 = plt.subplots(figsize=(10, 5))
# Create a second axis sharing the same x-axis
ax2 = ax1.twinx()

# Plot the series on their respective axes
_plot_series(ax1, test_dates, 'S&P 500', series_index=1)  # Plot S&P 500 on ax1
_plot_series(ax2, test_clean, 'Unemployment Rate', series_index=2) # Plot Unemployment Rate on ax2 (using cleaned data)

# Set titles and labels
ax1.set_title('S&P 500 vs Unemployment Rate (Dual Axis) (2015–2024)')
ax1.set_xlabel('Year')
ax1.set_ylabel('S&P 500 Index')
ax2.set_ylabel('Unemployment Rate (%)')

# Combine and display the legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines += lines2
labels += labels2
ax1.legend(lines, labels, loc='upper left')

# Adjust layout and show the plot
fig.tight_layout()
plt.show()

###--------------------------------------------------------------

"""---
### Percentage Change and Graphs
Using Inflation Rates
"""

# Inflation Index Plot

# Filter data to the desired date range
test_dates = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')
]

# Clean data for plotting (remove NaNs from PCE for consistent plotting)
test_clean = test_dates.dropna(subset=['PCE'])

# Setup the plot figure and axes
fig, ax = plt.subplots(figsize=(10, 5))

# Plot the inflation index series
_plot_series(ax, test_clean, 'PCE', series_index=0)
_plot_series(ax, test_clean, 'CPI', series_index=1)
_plot_series(ax, test_clean, 'Core PCE', series_index=2)
_plot_series(ax, test_clean, 'Core CPI', series_index=3)

# Set plot title, labels, and legend
ax.set_title('Inflation (2017–2024)')
ax.set_ylabel('Index')
ax.set_xlabel('Year')
ax.legend()

# Display the plot
plt.show()

# Inflation Percentage Change MoM & YoY Plot

# Filter data to the desired date range for plotting
plot_df = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')
].copy()

# Normalize dates to the 1st of each month for consistent monthly sampling (optional but recommended)
plot_df = plot_df[plot_df['Date'].dt.day == 1]

# Sort data by Date (important for plotting time series)
plot_df.sort_values('Date', inplace=True)

# Setup the plot figure and axes
fig, ax = plt.subplots(figsize=(10, 5))

# Plot the percentage change series using the pre-defined _plot_series function
_plot_series(ax, plot_df, 'CPI MoM %', 'CPI MoM', 0)
_plot_series(ax, plot_df, 'CPI YoY %', 'CPI YoY', 1)
_plot_series(ax, plot_df, 'PCE MoM %', 'PCE MoM', 2)
_plot_series(ax, plot_df, 'PCE YoY %', 'PCE YoY', 3)

# Set plot title, labels, and legend
ax.set_title('Inflation Rates: MoM and YoY')
ax.set_ylabel('%-Change')
ax.set_xlabel('Year')
ax.legend()

# Display the plot
plt.show()

# Inflation Percentage Change MoM & YoY Plot

# Filter data to the desired date range for plotting
plot_df = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')
].copy()

# Normalize dates to the 1st of each month for consistent monthly sampling (optional but recommended)
plot_df = plot_df[plot_df['Date'].dt.day == 1]

# Sort data by Date (important for plotting time series)
plot_df.sort_values('Date', inplace=True)

# Setup the plot figure and axes
fig, ax = plt.subplots(figsize=(10, 5))

# Plot the percentage change series using the pre-defined _plot_series function
_plot_series(ax, plot_df, 'Core CPI MoM %', 'Core CPI MoM', 0)
_plot_series(ax, plot_df, 'Core CPI YoY %', 'Core CPI YoY', 1)
_plot_series(ax, plot_df, 'Core PCE MoM %', 'Core PCE MoM', 2)
_plot_series(ax, plot_df, 'Core PCE YoY %', 'Core PCE YoY', 3)

# Set plot title, labels, and legend
ax.set_title('Inflation Rates: MoM and YoY')
ax.set_ylabel('%-Change')
ax.set_xlabel('Year')
ax.legend()

# Display the plot
plt.show()

"""---
### Advanced Graphs: Dual Axis, 4-in1, and Indexation
Using Production variables
"""

# Industrial Production
test_dates = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')
]
print(test_dates[['Date', 'Industrial Production']].dropna().tail())

# Capacity Utilization
test_dates = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')
]
print(test_dates[['Date', 'Capacity Utilization']].dropna().tail())

# Industrial Production (Simple Plot)

# Filter data to the desired date range
production_dates = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')
]

# Clean data for plotting (remove NaNs for Industrial Production)
production_clean = production_dates.dropna(subset=['Industrial Production'])

# Setup the plot figure and axes
fig, ax = plt.subplots(figsize=(10, 5))

# Plot the series using the pre-defined _plot_series function
_plot_series(ax, production_clean, 'Industrial Production', series_index=0)

# Set plot title, labels, and legend
ax.set_title('Industrial Production (2017–2024)')
ax.set_ylabel('Index')
ax.set_xlabel('Year')
ax.legend()

# Display the plot
plt.show()

# Capacity Utilization (Simple Plot)

# Filter to the desired date range
production_dates = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')
]

# Clean data for plotting (remove NaNs for Capacity Utilization)
capacity_clean = production_dates.dropna(subset=['Capacity Utilization'])

# Setup the plot figure and axes
fig, ax = plt.subplots(figsize=(10, 5))

# Plot the series using the pre-defined _plot_series function
_plot_series(ax, capacity_clean, 'Capacity Utilization', series_index=0)

# Set plot title, labels, and legend
ax.set_title('Capacity Utilization (2017–2024)')
ax.set_ylabel('Percent')
ax.set_xlabel('Year')
ax.legend()

# Display the plot
plt.show()

# Durable Goods Orders (Simple Plot)

# Filter to the desired date range
production_dates = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')
]

# Clean data for plotting (Note: Currently dropping NaNs based on 'Capacity Utilization' - review if this is intended)
# durable_clean = production_dates.dropna(subset=['Capacity Utilization']) # Original line
durable_clean = production_dates.dropna(subset=['Durable Goods Orders']) # Corrected: drop NaNs based on 'Durable Goods Orders'

# Setup the plot figure and axes
fig, ax = plt.subplots(figsize=(10, 5))

# Plot the series using the pre-defined _plot_series function
_plot_series(ax, durable_clean, 'Durable Goods Orders', series_index=0)

# Set plot title, labels, and legend
ax.set_title('Durable Goods Orders (2017–2024)')
ax.set_ylabel('Orders')
ax.set_xlabel('Year')
ax.legend()

# Display the plot
plt.show()

# Producer Price Index (Simple Plot)

# Filter to the desired date range
production_dates = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')
]

# Clean data for plotting (Note: Currently dropping NaNs based on 'Capacity Utilization' - review if this is intended)
# ppi_clean = production_dates.dropna(subset=['Capacity Utilization']) # Original line
ppi_clean = production_dates.dropna(subset=['Producer Price Index']) # Corrected: drop NaNs based on 'Producer Price Index'

# Setup the plot figure and axes
fig, ax = plt.subplots(figsize=(10, 5))

# Plot the series using the pre-defined _plot_series function
_plot_series(ax, ppi_clean, 'Producer Price Index', series_index=0)

# Set plot title, labels, and legend
ax.set_title('Producer Price Index (2017–2024)')
ax.set_ylabel('Index')
ax.set_xlabel('Year')
ax.legend()

# Display the plot
plt.show()

# Production Overview: Dual Y-Axis Plot

# Filter data to the desired date range
production_dates = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')
]

# Clean individual series by dropping NaNs for each specific variable
production_clean = production_dates.dropna(subset=['Industrial Production'])
capacity_clean = production_dates.dropna(subset=['Capacity Utilization'])
durable_clean = production_dates.dropna(subset=['Durable Goods Orders'])
ppi_clean = production_dates.dropna(subset=['Producer Price Index'])

# Setup plot with two y-axes
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()  # Second y-axis on the right

# Plot series on their respective axes
# Left y-axis (Industrial Production and Capacity Utilization)
_plot_series(ax1, production_clean, 'Industrial Production', series_index=0)
_plot_series(ax1, capacity_clean, 'Capacity Utilization', series_index=1)

# Right y-axis (Durable Goods Orders and Producer Price Index)
_plot_series(ax2, durable_clean, 'Durable Goods Orders', series_index=2)
_plot_series(ax2, ppi_clean, 'Producer Price Index', series_index=3)

# Set titles and labels
ax1.set_title('Production Overview: Dual Y-Axis (2017–2024)')
ax1.set_ylabel('Industrial Prod. / Capacity Utilization')
ax2.set_ylabel('Durable Goods Orders / PPI')

# Combine and display the legend
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

# Improve plot appearance
sns.despine()
fig.tight_layout()
plt.show()

# Production Indicators: 4-in-1 Plot

# Filter data to the desired date range
production_dates = filtered_df[
    (filtered_df['Date'] >= '2016-01-01') & (filtered_df['Date'] <= '2024-12-31')
]

# Clean individual series by dropping NaNs
production_clean = production_dates.dropna(subset=['Industrial Production'])
capacity_clean = production_dates.dropna(subset=['Capacity Utilization'])
durable_clean = production_dates.dropna(subset=['Durable Goods Orders'])
ppi_clean = production_dates.dropna(subset=['Producer Price Index'])

# Setup a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharex=True)

# Plot each series on its respective subplot using the pre-defined _plot_series function
_plot_series(axes[0, 0], production_clean, 'Industrial Production', series_index=1)
_plot_series(axes[0, 1], capacity_clean, 'Capacity Utilization', series_index=2)
_plot_series(axes[1, 0], durable_clean, 'Durable Goods Orders', series_index=3)
_plot_series(axes[1, 1], ppi_clean, 'Producer Price Index', series_index=4)

# Set titles for each subplot
axes[0, 0].set_title('Industrial Production')
axes[0, 1].set_title('Capacity Utilization')
axes[1, 0].set_title('Durable Goods Orders')
axes[1, 1].set_title('Producer Price Index')

# Set a main title for the entire figure
fig.suptitle('Production Indicators (2016–2024)', fontsize=14)

# Adjust layout to prevent overlapping titles and labels
fig.tight_layout()

# Show the plot
plt.show()

# Production Indicators: Rebased Plot / Indexed at 100

# Filter data to the desired date range
production_dates = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')
].copy()

# Drop NaNs for the selected columns to ensure consistent rebasing
required_columns = ['Industrial Production', 'Capacity Utilization', 'Durable Goods Orders', 'Producer Price Index']
production_clean = production_dates.dropna(subset=required_columns).copy()

# Sort by date (important for correct rebasing to the first observation)
production_clean.sort_values('Date', inplace=True)

# Normalize each series to 100 at the first observation (after sorting)
for col in required_columns:
    first_value = production_clean[col].iloc[0]
    production_clean[f'{col} (Rebased)'] = production_clean[col] / first_value * 100

# Setup the plot figure and axes
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the rebased series using the pre-defined _plot_series function
_plot_series(ax, production_clean, 'Industrial Production (Rebased)', series_index=0)
_plot_series(ax, production_clean, 'Capacity Utilization (Rebased)', series_index=1)
_plot_series(ax, production_clean, 'Durable Goods Orders (Rebased)', series_index=2)
_plot_series(ax, production_clean, 'Producer Price Index (Rebased)', series_index=3)

# Set plot title, labels, and legend
ax.set_title('Production Indicators (Rebased to 100 at Jan 2017)')
ax.set_ylabel('Index (100 = Jan 2017)')
ax.legend(loc='upper left')

# Improve plot appearance
sns.despine()
fig.tight_layout()
plt.show()

###--------------------------------------------------------------

"""---
### Moving Averages and Trend Lines
Using Inflation Numbers
"""

# Calculate moving averages for trendlines (e.g., 12-month moving average)
window_size = 12

# List of columns to calculate moving averages for
# Use the correct column names created in the percentage change step
columns_to_trendline = ['PCE YoY %', 'CPI YoY %', 'Core PCE YoY %', 'Core CPI YoY %']

# Create a new DataFrame from monthly_df for the trend calculations
# This ensures the original monthly_df is not modified and is good practice
monthly_ma_df = monthly_df.copy()

for col in columns_to_trendline:
    # Calculate the moving average, aligning to the right (so the average includes the current data point)
    monthly_ma_df[f'{col}_trend'] = monthly_ma_df[col].rolling(window=window_size, center=False).mean()

# Inflation Trend Lines Plot

# Filter monthly_ma_df to the desired date range
monthly_ma_df = monthly_ma_df[
    (monthly_ma_df['Date'] >= '2017-01-01') & (monthly_ma_df['Date'] <= '2024-12-31')
]

# Setup the plot figure and axes
fig, ax = plt.subplots(figsize=(10, 5))

# Plot the trendlines for the desired series
_plot_series(ax, monthly_ma_df, 'PCE YoY %_trend', 'PCE YoY (trend)', 0)
_plot_series(ax, monthly_ma_df, 'CPI YoY %_trend', 'CPI YoY (trend)', 1)
_plot_series(ax, monthly_ma_df, 'Core PCE YoY %_trend', 'Core PCE YoY (trend)', 2)
_plot_series(ax, monthly_ma_df, 'Core CPI YoY %_trend', 'Core CPI YoY (trend)', 3)

# Set plot title, labels, and legend
ax.set_title('Inflation Trend Lines')
ax.set_ylabel('%-Change')
ax.set_xlabel('Year')
ax.legend()

# Display the plot
plt.show()


###--------------------------------------------------------------

"""---
### Correlations Matrixes, OLS, and Regressions
Using Inflation Numbers
"""

# Correlation Matrix of YoY Inflation Metrics

# Select the percentage change columns for the correlation analysis
# Use filtered_df which contains the percentage change columns from Step 7.1
corr_data = filtered_df[['CPI YoY %', 'PCE YoY %', 'Core CPI YoY %', 'Core PCE YoY %']]

# Compute the correlation matrix
corr_matrix = corr_data.corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Correlation Matrix of YoY Inflation Metrics")

# Ensure plot is displayed correctly
plt.tight_layout()
plt.show()

# OLS Trendline for CPI YoY Plot

# Prepare CPI data over time
# Use filtered_df which contains the 'CPI YoY %' column (from Step 7.1)
df = filtered_df.dropna(subset=['CPI YoY %']).copy() # Use .copy() to avoid SettingWithCopyWarning

# Ensure Date is datetime and sorted (important for the time index and plotting)
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

# Perform OLS regression to find the trendline
X = sm.add_constant(range(len(df)))  # Time index
y = df['CPI YoY %'] # Use the correct column name
model = sm.OLS(y, X).fit()
df['Trend_CPI_YoY'] = model.predict(X)

# Plot the original data and the OLS trendline
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['CPI YoY %'], label='CPI YoY') # Use the correct column name here too
plt.plot(df['Date'], df['Trend_CPI_YoY'], label='OLS Trendline', linestyle='--')

# Set plot title, labels, and legend
plt.legend()
plt.title("OLS Trendline for CPI YoY")
plt.ylabel('% Change')
plt.xlabel('Date')

# Improve plot appearance
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Show the plot
plt.show()

# 12-Month Rolling Correlation: Core CPI vs Core PCE Plot

# Calculate the 12-month rolling correlation
# Use monthly_df (created in Step 8) which has a consistent monthly frequency
rolling_corr = monthly_df['Core CPI YoY %'].rolling(12).corr(monthly_df['Core PCE YoY %'])

# Setup the plot
plt.figure(figsize=(10, 5))

# Plot the rolling correlation over time
# Use the Date column from monthly_df for the x-axis
plt.plot(monthly_df['Date'], rolling_corr)

# Set plot title and labels
plt.title('12-Month Rolling Correlation: Core CPI vs Core PCE')
plt.ylabel('Correlation')
plt.xlabel('Date')

# Improve plot appearance
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Show the plot
plt.show()

# Create 3-month lag of Fed Funds Rate directly on monthly_df
# Ensure 'Federal Funds Rate' exists in monthly_df after the merge
monthly_df['Fed_Funds_Rate_lag3'] = monthly_df['Federal Funds Rate'].shift(3)

# Now drop NaNs for the required columns
# Drop NaNs specifically for the columns used in the regression model
lag_df = monthly_df.dropna(subset=['Fed_Funds_Rate_lag3', 'CPI YoY %']).copy()

# Check if lag_df is empty before proceeding
if lag_df.empty:
    print("Error: The DataFrame for regression is empty after dropping NaNs.")
else:
    # Regression: lagged FFR predicting current CPI YoY
    X = sm.add_constant(lag_df['Fed_Funds_Rate_lag3'])
    y = lag_df['CPI YoY %']
    model_lag = sm.OLS(y, X).fit()

    print(model_lag.summary())

###--------------------------------------------------------------

"""### Regression, Robust SE, Multicollinearity, Heteroskedasticity, Serial Correlation, and Standardized Betas

Robust SE:
(HAC or White)

Multicollinearity:
Variance Inflation Factor (VIF)

Heteroskedasticity:
White's Test

Serial Correlation:
Durbin-Watson Test

Standardized Betas: (β Coefficients)




"""

# Macro Indicators Overview: Dual Y-Axis Plot

# Filter data to the desired date range
macro_dates = filtered_df[
    (filtered_df['Date'] >= '2017-01-01') & (filtered_df['Date'] <= '2024-12-31')].copy()

# Drop NaNs for all relevant columns to ensure a consistent dataset for plotting
required_columns = ['Unemployment Rate', 'Retail Sales', 'CPI', 'Industrial Production']
macro_clean = macro_dates.dropna(subset=required_columns).copy()

# Sort by date (important for plotting time series and indexing)
macro_clean.sort_values('Date', inplace=True)

# Setup plot with two y-axes
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()

# Plot Unemployment Rate on the left Y-axis
_plot_series(ax1, macro_clean, 'Unemployment Rate', series_index=0)

# Plot other variables on the right Y-axis (normalized for comparability)
for i, col in enumerate(['Retail Sales', 'CPI', 'Industrial Production']):
    # Normalize the series to 100 at the first data point
    normalized = macro_clean[col] / macro_clean[col].iloc[0] * 100
    # Plot the normalized series on the second axis
    ax2.plot(macro_clean['Date'], normalized, label=col + ' (Indexed)',
             color=sns.color_palette('Dark2')[i + 1]) # Use a different color from palette

# Set titles and labels for both axes
ax1.set_title('Unemployment Rate, Retail Sales, CPI, and Industrial Production (2017–2024)')
ax1.set_xlabel('Year')
ax1.set_ylabel('Unemployment Rate (%)')
ax2.set_ylabel('Indexed Level (100 = Jan 2017)')

# Combine and display the legend from both axes
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left')

# Improve plot appearance
sns.despine() # Remove top and right spines
fig.tight_layout() # Adjust layout to prevent overlapping elements
plt.show()

# Normal Regression

# Drop NA rows for regression, only considering the columns used in the model
# Define dependent and independent variables
y_col = 'Unemployment Rate'
X_cols = ['Retail Sales', 'CPI YoY %', 'Industrial Production']

# Ensure the columns exist before dropping NaNs
required_cols_for_reg = [y_col] + X_cols
# Drop NaNs specifically for the columns needed for this regression model
reg_df = monthly_df.dropna(subset=required_cols_for_reg).copy()

# Check if reg_df is empty after dropping NaNs
if reg_df.empty:
    print("Error: The DataFrame for regression is empty after dropping NaNs for the selected columns.")
else:
    y = reg_df[y_col]
    X = reg_df[X_cols]
    X = sm.add_constant(X)  # add intercept

    ols_model = sm.OLS(y, X).fit()
    print(ols_model.summary())

# The following cells also use reg_df and ols_model, so ensure they handle the case where reg_df might still be empty
# Add similar empty checks or ensure this cell runs only if reg_df is not empty

# White's Model for Robust SE
robust_model = ols_model.get_robustcov_results(cov_type='HC1')  # White's correction
print(robust_model.summary())

# HAC-model for Robust SE
hac_model = ols_model.get_robustcov_results(cov_type='HAC', maxlags=1)
print(hac_model.summary())

# Multicollinearity - VIF
vif_data = pd.DataFrame()
vif_data["Variable"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif_data)

# Heteroskedasticity – White’s Test

### White's heteroskedasticity test requires exog to have at least two columns, where one is a constant.
### white_test = het_white(ols_model.resid, X)
### labels = ['Test Statistic', 'Test p-value', 'F-Statistic', 'F-Test p-value']
### print(lzip(labels, white_test))

# Serial Correlation – Durbin-Watson Test
dw_stat = durbin_watson(ols_model.resid)
print(f"Durbin-Watson Statistic: {dw_stat}")

# Standardized Betas (β Coefficients)

# Initialize StandardScaler
scaler = StandardScaler()

# Standardize the independent variables (excluding the constant)
X_std = scaler.fit_transform(X.drop(columns='const'))

# Standardize the dependent variable
y_std = scaler.fit_transform(y.values.reshape(-1, 1)).flatten()

# Re-add the constant term to the standardized independent variables
X_std = sm.add_constant(X_std)

# Fit the OLS model using the standardized variables
standardized_model = sm.OLS(y_std, X_std).fit()

# Print the summary of the standardized regression model
print(standardized_model.summary())

