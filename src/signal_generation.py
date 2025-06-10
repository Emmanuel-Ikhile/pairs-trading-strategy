import pandas as pd
import os

# Load spread data
spread_path = os.path.join("data", "processed", "spread_features.csv")
df = pd.read_csv(spread_path, parse_dates=["Date"])

# Initialize Signal column
df["Signal"] = 0

# Entry and exit logic
df.loc[df["Z_Score"] > 1.0, "Signal"] = -1  # Short
df.loc[df["Z_Score"] < -1.0, "Signal"] = 1  # Long
df.loc[df["Z_Score"].abs() < 0.1, "Signal"] = 0  # Exit near mean (tighter band for cleaner exits)

# Create Position column (shifted signal to simulate next-day position)
df["Position"] = df["Signal"].shift()

# Save to new processed file
output_path = os.path.join("data", "processed", "spread_with_signals.csv")
df.to_csv(output_path, index=False)

print(f"✅ Signals generated and saved to {output_path}")
