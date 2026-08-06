import pandas as pd

data = pd.read_csv("sample_market_data.csv")

print("----- Trading System Monitoring -----\n")

for _, row in data.iterrows():

    symbol = row["Symbol"]
    price = row["Price"]
    previous = row["PreviousPrice"]
    timestamp = row["Timestamp"]

    if pd.isna(price):
        print(f"[ALERT] Missing market price for {symbol}")
        continue

    if price < 0:
        print(f"[ALERT] Negative price detected for {symbol}")

    if timestamp != "09:30":
        print(f"[WARNING] Stale market data received for {symbol}")

    change = abs((price - previous) / previous)

    if change > 0.10:
        print(f"[WARNING] Large price movement detected for {symbol} ({change:.2%})")

print("\nMonitoring complete.")
