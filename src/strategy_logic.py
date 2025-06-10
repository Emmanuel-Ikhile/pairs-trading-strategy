import pandas as pd
import os

# Set paths
data_dir = os.path.join("data", "processed")
apple_path = os.path.join(data_dir, "apple_features.csv")
msft_path = os.path.join(data_dir, "microsoft_features.csv")

# Load data
apple = pd.read_csv(apple_path, parse_dates=['Date'])
msft = pd.read_csv(msft_path, parse_dates=['Date'])

# Merge on Date (inner join to match dates)
merged = pd.merge(apple[['Date', 'Close']], msft[['Date', 'Close']],
                  on='Date', suffixes=('_AAPL', '_MSFT'))

# Compute spread (difference and ratio)
merged['Price_Diff'] = merged['Close_AAPL'] - merged['Close_MSFT']
merged['Price_Ratio'] = merged['Close_AAPL'] / merged['Close_MSFT']

# Compute Z-score of the Price_Diff (rolling 30-day window)
window = 30
merged['Z_Score'] = (merged['Price_Diff'] - merged['Price_Diff'].rolling(window).mean()) / merged['Price_Diff'].rolling(window).std()

# Drop NaNs from rolling
merged.dropna(inplace=True)

# Save to processed folder
output_path = os.path.join(data_dir, "spread_features.csv")
merged.to_csv(output_path, index=False)

print(f"✅ Spread data saved to: {output_path}")
