import pandas as pd

def simulate_price_change(df, price_change_pct):
    
    df_copy = df.copy()
    
    df_copy["new_price"] = df_copy["price"] * (1 + price_change_pct/100)
    df_copy["new_revenue"] = df_copy["new_price"] + df_copy["freight_value"]
    df_copy["new_cost"] = 0.65 * df_copy["new_price"] + df_copy["freight_value"]
    df_copy["new_profit"] = df_copy["new_revenue"] - df_copy["new_cost"]
    
    return df_copy["new_profit"].sum()


def simulate_by_category(df, category, price_change_pct):
    
    df_copy = df.copy()
    
    mask = df_copy["product_category_name"] == category
    
    df_copy.loc[mask, "new_price"] = df_copy.loc[mask, "price"] * (1 + price_change_pct/100)
    df_copy["new_price"] = df_copy["new_price"].fillna(df_copy["price"])
    
    df_copy["new_revenue"] = df_copy["new_price"] + df_copy["freight_value"]
    df_copy["new_cost"] = 0.65 * df_copy["new_price"] + df_copy["freight_value"]
    df_copy["new_profit"] = df_copy["new_revenue"] - df_copy["new_cost"]
    
    return df_copy["new_profit"].sum()


def recommend_price_change(df):
    
    base_profit = df["Profit"].sum()
    
    increase = simulate_price_change(df, 5)
    decrease = simulate_price_change(df, -5)
    
    if increase > base_profit:
        return "Increase prices recommended"
    elif decrease > base_profit:
        return "Decrease prices recommended"
    else:
        return "Keep prices same"