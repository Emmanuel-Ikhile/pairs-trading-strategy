import yfinance as yf

# Download 10 years of data
apple = yf.download('AAPL', start='2015-01-01', end='2025-01-01')
microsoft = yf.download('MSFT', start='2015-01-01', end='2025-01-01')

# Save the data locally in the existing 'data' folder
apple.to_csv('data/AAPL.csv')
microsoft.to_csv('data/MSFT.csv')

print("Data downloaded and saved successfully.")

