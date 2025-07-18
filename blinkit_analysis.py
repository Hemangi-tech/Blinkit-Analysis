import pandas as pd

# Step 1: Load all files (update filenames if needed)
orders = pd.read_csv("blinkit_orders.csv")
order_items = pd.read_csv("blinkit_order_items.csv")
products = pd.read_csv("blinkit_products.csv")
customers = pd.read_csv("blinkit_customers.csv")

# Step 2: Merge order_items with orders to get order_date, customer_id, etc.
df1 = pd.merge(order_items, orders, on="order_id", how="left")

# Step 3: Merge with products to get product details
df2 = pd.merge(df1, products, on="product_id", how="left")

# Step 4: Merge with customers to get location details (area, pincode)
final_df = pd.merge(df2, customers, on="customer_id", how="left")

# Step 5: Convert order_date to datetime
final_df['order_date'] = pd.to_datetime(final_df['order_date'], errors='coerce')

# Step 6: Create time-based fields for trend analysis
final_df['Month'] = final_df['order_date'].dt.month_name()
final_df['Day'] = final_df['order_date'].dt.day_name()
final_df['Hour'] = final_df['order_date'].dt.hour

# Step 7: Create total value column
final_df['total_value'] = final_df['quantity'] * final_df['unit_price']
total_orders = final_df['order_id'].nunique()
# Step 8: Export cleaned data for Power BI
final_df.to_csv("blinkit_cleaned_demand_data.csv", index=False)
