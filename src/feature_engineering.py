import yfinance as yf
import pandas as pd
from arch import arch_model
import os

def download_data(ticker, start='2015-01-01', end='2025-01-01'):
    df = yf.download(ticker, start=start, end=end)
    df.dropna(inplace=True)
    return df

def engineer_features(df):
    df['Daily_Return'] = df['Close'].pct_change()
    df['Rolling_Mean'] = df['Daily_Return'].rolling(window=20).mean()
    df['Rolling_Std'] = df['Daily_Return'].rolling(window=20).std()
    df['Rolling_Volatility'] = df['Daily_Return'].rolling(window=20).std()

    high_low = df['High'] - df['Low']
    high_close_prev = (df['High'] - df['Close'].shift()).abs()
    low_close_prev = (df['Low'] - df['Close'].shift()).abs()
    true_range = pd.concat([high_low, high_close_prev, low_close_prev], axis=1).max(axis=1)
    df['ATR'] = true_range.rolling(window=14).mean()

    returns = df['Daily_Return'].dropna() * 100  # percent returns for stability in arch model
    garch_model = arch_model(returns, vol='Garch', p=1, q=1)
    garch_result = garch_model.fit(disp='off')
    df.loc[returns.index, 'GARCH_Volatility'] = garch_result.conditional_volatility / 100  # back to decimals

    return df

def main():
    # Download data
    apple = download_data('AAPL')
    microsoft = download_data('MSFT')

    # Engineer features
    apple = engineer_features(apple)
    microsoft = engineer_features(microsoft)

    # Create folder if it doesn't exist
    if not os.path.exists('data/processed'):
        os.makedirs('data/processed')

    # Save to CSV
    apple.to_csv('data/processed/apple_features.csv')
    microsoft.to_csv('data/processed/microsoft_features.csv')

    print("Feature engineering completed and files saved.")

if __name__ == "__main__":
    main()
