# Volatility-Driven Pairs Trading Strategy: AAPL vs. MSFT
A Python Data Analysis Project by Emmanuel IKHILE

 A complete data analysis pipeline from raw stock data to a backtested trading strategy, focusing on volatility patterns and statistical arbitrage opportunities between Apple and Microsoft.

## Project Highlights

- Full EDA workflow from data collection to actionable insights
- Professional-grade feature engineering (GARCH, ATR, rolling volatility)
- Complete trading strategy with entry/exit rules and backtesting
- Production-ready code structure with clear documentation

## Key Features

**Data Collection & Engineering**

Collected 10 years of daily OHLCV data for AAPL/MSFT using yfinance


**Engineered advanced volatility features**

Rolling volatility (20-day)

Average True Range (ATR)

GARCH(1,1) volatility estimates

Calculated spread metrics and Z-scores for pairs trading


**Exploratory Data Analysis**

Identified volatility clustering patterns

Detected regime shifts (e.g., COVID-19 market impact)

Analyzed spread behavior for mean-reversion opportunities


**Trading Strategy Implementation**
python

**Signal generation logic**
df['Signal'] = np.where(df['Z_Score'] <= -1, 1, 
                      np.where(df['Z_Score'] >= 1, -1, 0))
Z-score based entry/exit signals

Forward-filled positions to simulate holding periods

Complete backtesting framework


**Performance Evaluation**

Calculated strategy returns and drawdowns

Visualized performance vs. buy-and-hold

Identified periods of strategy effectiveness


## Key Lessons Learned
***Volatility Timing Matters:***

Rolling metrics introduce lag - critical to avoid lookahead bias

GARCH models better capture volatility persistence but are computationally expensive


***Simple ≠ Ineffective***

Basic Z-score approach generated viable signals without complex econometrics

Clear, interpretable strategies are easier to debug and improve


***Data Quality is Everything***

Missing values in raw data required careful handling

Feature scaling dramatically impacts strategy performance


***Visualization is Powerfu***l

Plotting entry/exit points revealed flaws in signal logic

Cumulative return charts quickly show strategy viability


**🛠️ Technical Stack**


- Data Collection	- yfinance
- Data Processing -	pandas, numpy
- Visualization	- matplotlib, seaborn
- Volatility Modeling	- arch (GARCH)
- Development	- VS Code


**🚧 Future Improvements**

- Add formal cointegration testing

- Implement walk-forward optimization

- Build interactive dashboard with Plotly/Dash

- Add risk management module (position sizing, stop-loss)


📧 Contact: [emmaikhile34@gmail.com] | 🔗 [[LinkedIn Profile](https://www.linkedin.com/in/emmanuel-ikhile-2436b0258)]

⚖️ License: MIT
