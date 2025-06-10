import pandas as pd
import os

# Load signal data
input_path = os.path.join("data", "processed", "spread_with_signals.csv")
df = pd.read_csv(input_path, parse_dates=["Date"])

# Replace chained assignment with safe alternatives
df["Signal"] = df["Signal"].fillna(0)
df["Position"] = df["Signal"].shift(1).fillna(0)

# Use 'Price_Diff' as the spread
spread_col = "Price_Diff"

# Calculate strategy return based on percentage change in spread
df["Strategy_Return"] = df[spread_col].pct_change() * df["Position"]
df["Cumulative_Strategy_Return"] = (1 + df["Strategy_Return"]).cumprod()

# Save results
output_path = os.path.join("data", "processed", "backtest_results.csv")
df.to_csv(output_path, index=False)

print("✅ Backtest results saved to:", output_path)

