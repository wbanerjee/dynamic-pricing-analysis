import pandas as pd
from simulation import simulate_price_change, simulate_by_category, recommend_price_change

# Load data
df = pd.read_csv("../data/master_dataset.csv")

# Baseline
current_profit = df["Profit"].sum()
print(f"Current Profit: {current_profit:.2f}")

# Simulate overall price change
change_pct = 5
new_profit = simulate_price_change(df, change_pct)

print(f"\nProfit after {change_pct}% price increase: {new_profit:.2f}")

profit_change = ((new_profit - current_profit) / current_profit) * 100
print(f"Profit Change: {profit_change:.2f}%")

# Category simulation
category = "beleza_saude"
cat_profit = simulate_by_category(df, category, 5)

print(f"\nProfit after 5% increase in {category}: {cat_profit:.2f}")

# Recommendation
decision = recommend_price_change(df)
print(f"\nRecommendation: {decision}")