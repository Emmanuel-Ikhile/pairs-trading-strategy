import os
import pandas as pd
import matplotlib.pyplot as plt

# Set base directories
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
processed_dir = os.path.join(base_dir, 'data', 'processed')
plots_dir = os.path.join(base_dir, 'plots')

# Create ticker-specific folders for plots
tickers = ['apple', 'microsoft']
for ticker in tickers:
    os.makedirs(os.path.join(plots_dir, ticker), exist_ok=True)

# Load data
apple_df = pd.read_csv(os.path.join(processed_dir, 'apple_features.csv'))
microsoft_df = pd.read_csv(os.path.join(processed_dir, 'microsoft_features.csv'))

# Convert 'Date' column to datetime
apple_df['Date'] = pd.to_datetime(apple_df['Date'])
microsoft_df['Date'] = pd.to_datetime(microsoft_df['Date'])

# Features to plot
plot_features = {
    'Close': 'Closing Price',
    'Daily_Return': 'Daily Return',
    'Rolling_Mean': 'Rolling Mean',
    'Rolling_Std': 'Rolling Std Dev',
    'Rolling_Volatility': 'Rolling Volatility',
    'ATR': 'Average True Range (ATR)',
    'GARCH_Volatility': 'GARCH Volatility'
}

# Plotting function
def plot_and_save(df, ticker, column, ylabel, output_folder):
    # Drop rows with missing values
    clean_df = df[['Date', column]].dropna()

    plt.figure(figsize=(12, 6))
    plt.plot(clean_df['Date'], clean_df[column])
    plt.title(f"{ticker.upper()} - {ylabel}")
    plt.xlabel("Date")
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()

    # Save plot
    filename = f"{column.lower().replace(' ', '_')}.png"
    filepath = os.path.join(output_folder, filename)
    plt.savefig(filepath)
    plt.close()
    print(f"Saved: {filepath}")

# Loop through each ticker and plot
for ticker, df in zip(tickers, [apple_df, microsoft_df]):
    output_folder = os.path.join(plots_dir, ticker)
    for column, label in plot_features.items():
        if column in df.columns:
            plot_and_save(df, ticker, column, label, output_folder)
