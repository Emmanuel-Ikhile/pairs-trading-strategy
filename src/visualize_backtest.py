import pandas as pd
import matplotlib.pyplot as plt
import os

# Load backtest results
input_path = os.path.join("data", "processed", "backtest_results.csv")
df = pd.read_csv(input_path, parse_dates=["Date"])

# Ensure the 'plots/backtest' directory exists
plot_dir = os.path.join("plots", "backtest")
os.makedirs(plot_dir, exist_ok=True)

# Plot 1: Spread + Buy/Sell Signals
plt.figure(figsize=(14, 6))
plt.plot(df["Date"], df["Price_Diff"], label="Price Difference (Spread)", color="blue")
plt.plot(df["Date"][df["Signal"] == 1], df["Price_Diff"][df["Signal"] == 1], "^", markersize=10, color="green", label="Buy Signal")
plt.plot(df["Date"][df["Signal"] == -1], df["Price_Diff"][df["Signal"] == -1], "v", markersize=10, color="red", label="Sell Signal")
plt.title("Spread with Buy/Sell Signals")
plt.xlabel("Date")
plt.ylabel("Price Difference")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, "spread_signals.png"))
plt.close()

# Plot 2: Cumulative Strategy Returns
plt.figure(figsize=(14, 6))
plt.plot(df["Date"], df["Cumulative_Strategy_Return"], label="Cumulative Return", color="purple")
plt.title("Cumulative Return of Pairs Trading Strategy")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, "cumulative_returns.png"))
plt.close()

print("✅ Backtest plots saved in:", plot_dir)
