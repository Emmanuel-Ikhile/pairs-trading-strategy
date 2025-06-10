import pandas as pd
import matplotlib.pyplot as plt
import os

# Set up paths
data_dir = os.path.join('data', 'processed')
plot_dir = os.path.join('plots', 'feature_comparison')
os.makedirs(plot_dir, exist_ok=True)

# Load datasets
apple_df = pd.read_csv(os.path.join(data_dir, 'apple_features.csv'), parse_dates=['Date'])
msft_df = pd.read_csv(os.path.join(data_dir, 'microsoft_features.csv'), parse_dates=['Date'])

# Drop rows with missing values to align plots
apple_df.dropna(inplace=True)
msft_df.dropna(inplace=True)

# Ensure same date alignment for comparison plots
merged = pd.merge(apple_df, msft_df, on='Date', suffixes=('_AAPL', '_MSFT'))

# --- 1. Daily Returns Comparison ---
plt.figure(figsize=(14, 6))
plt.plot(merged['Date'], merged['Daily_Return_AAPL'], label='Apple Daily Return', color='red')
plt.plot(merged['Date'], merged['Daily_Return_MSFT'], label='Microsoft Daily Return', color='blue')
plt.title('Daily Returns Comparison: Apple vs Microsoft')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, 'daily_returns_comparison.png'))
plt.close()

# --- 2. Price Spread (AAPL - MSFT) ---
merged['Price_Spread'] = merged['Close_AAPL'] - merged['Close_MSFT']
plt.figure(figsize=(14, 6))
plt.plot(merged['Date'], merged['Price_Spread'], label='Price Spread (Apple - Microsoft)', color='purple')
plt.title('Price Spread Between Apple and Microsoft')
plt.xlabel('Date')
plt.ylabel('Price Spread (USD)')
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, 'price_spread.png'))
plt.close()

# --- 3. Rolling Volatility Comparison ---
plt.figure(figsize=(14, 6))
plt.plot(merged['Date'], merged['Rolling_Volatility_AAPL'], label='Apple Volatility', color='crimson')
plt.plot(merged['Date'], merged['Rolling_Volatility_MSFT'], label='Microsoft Volatility', color='darkgreen')
plt.title('Rolling Volatility Comparison')
plt.xlabel('Date')
plt.ylabel('Rolling Std Deviation')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, 'rolling_volatility_comparison.png'))
plt.close()

print("✅ All plots generated and saved in: plots/feature_comparison/")
