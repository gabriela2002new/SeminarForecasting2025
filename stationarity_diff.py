import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# Load the Excel data
file_path = '/Users/pansitie/Desktop/Map1.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Display the first few rows to understand the structure of the data
print(df.head())

# Assuming 'Date' is a column in your data, let's set it as the index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# List of columns to take the first difference
columns_to_diff = ['Headline HCIP', 'Brent', 'EU Average Electricity Price',
                   'Gas Prices', 'Unemployment Rate', 'GSCPI', 'GDP_M']

# Take the first difference of all relevant columns
df_diff = df[columns_to_diff].diff().dropna()  # Drop NaN values after taking the diff

# Plot each first-differenced time series separately
for column in columns_to_diff:
    plt.figure(figsize=(10, 6))  # Create a new figure for each plot
    df_diff[column].plot()
    plt.title(f'First Difference of {column}')
    plt.xlabel('Date')
    plt.ylabel('First Difference')
    plt.legend([column], loc='best')
    plt.show()

# Perform Augmented Dickey-Fuller Test for stationarity
def adf_test(series, column_name):
    result = adfuller(series.dropna())  # Drop NaN values for the test
    print(f"ADF Test for {column_name}:")
    print(f"ADF Statistic: {result[0]}")
    print(f"p-value: {result[1]}")
    print(f"Critical Values: {result[4]}")
    print("Null Hypothesis: Data has a unit root (Non-stationary)")
    print("Alternate Hypothesis: Data is stationary")
    print("-" * 50)

# Apply ADF test on the first-differenced series
for column in columns_to_diff:
    adf_test(df_diff[column], column)
