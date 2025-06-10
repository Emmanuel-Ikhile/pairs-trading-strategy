import yfinance as yf

# Download 10 years of data for Apple and Microsoft
apple = yf.download('AAPL', start='2015-01-01', end='2025-01-01')
microsoft = yf.download('MSFT', start='2015-01-01', end='2025-01-01')

# Preview first 5 rows of Apple data
print("Apple Data Preview:")
print(apple.head())

print("\nMicrosoft Data Preview:")
print(microsoft.head())

# Minor EDA for Apple
print("\nApple Data Info:")
print(apple.info())

print("\nApple Data Description:")
print(apple.describe())

# Minor EDA for Microsoft
print("\nMicrosoft Data Info:")
print(microsoft.info())

print("\nMicrosoft Data Description:")
print(microsoft.describe())
