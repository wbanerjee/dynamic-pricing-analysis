import streamlit as st
import pandas as pd
from simulation import simulate_price_change, simulate_by_category, recommend_price_change

# Load data
df = pd.read_csv("../data/master_dataset.csv")

# Title
st.title("📊 Dynamic Pricing Simulation Tool")

st.markdown("""
This tool simulates how price changes impact profit and provides recommendations.
""")

# Sidebar inputs
st.sidebar.header("Controls")

price_change = st.sidebar.slider(
    "Select Price Change (%)",
    min_value=-20,
    max_value=20,
    value=5
)

category = st.sidebar.selectbox(
    "Select Category",
    options=df["product_category_name"].dropna().unique()
)

# Baseline
current_profit = df["Profit"].sum()

# Simulations
new_profit = simulate_price_change(df, price_change)
cat_profit = simulate_by_category(df, category, price_change)

profit_change = ((new_profit - current_profit) / current_profit) * 100

# Display KPIs
st.subheader("📈 Overall Impact")

col1, col2, col3 = st.columns(3)

col1.metric("Current Profit", f"{current_profit:,.0f}")
col2.metric("New Profit", f"{new_profit:,.0f}")
col3.metric("Change (%)", f"{profit_change:.2f}%")

# Category result
st.subheader("📦 Category Impact")

st.write(f"Profit after {price_change}% change in **{category}**:")
st.write(f"{cat_profit:,.0f}")

# Recommendation
st.subheader("💡 Recommendation")

decision = recommend_price_change(df)
st.success(decision)