import pandas as pd
import matplotlib.pyplot as plt
import os

# Load spread data
spread_path = os.path.join("data", "processed", "spread_features.csv")
df = pd.read_csv(spread_path, parse_dates=["Date"])

# Create plots directory if it doesn't exist
plot_dir = os.path.join("plots", "spread")
os.makedirs(plot_dir, exist_ok=True)

# Plot 1: Z-score with upper/lower thresholds
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Z_Score'], label='Z-Score', color='darkblue')
plt.axhline(1.0, color='red', linestyle='--', label='Upper Threshold (+1)')
plt.axhline(-1.0, color='green', linestyle='--', label='Lower Threshold (-1)')
plt.axhline(0, color='black', linestyle='-')
plt.title("Z-Score of Price Difference (AAPL - MSFT)")
plt.xlabel("Date")
plt.ylabel("Z-Score")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, "z_score.png"))
plt.close()

# Plot 2: Price Difference
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Price_Diff'], label='Price Difference', color='purple')
plt.title("Price Difference: AAPL - MSFT")
plt.xlabel("Date")
plt.ylabel("Price Difference (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, "price_difference.png"))
plt.close()

# Plot 3: Price Ratio
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Price_Ratio'], label='Price Ratio', color='orange')
plt.title("Price Ratio: AAPL / MSFT")
plt.xlabel("Date")
plt.ylabel("Ratio")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, "price_ratio.png"))
plt.close()

print(f"✅ Spread plots saved to: {plot_dir}")
