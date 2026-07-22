7. Scenario: You are working as a data analyst for an e-commerce company. You have been given a
dataset containing information about customer orders, stored in a Pandas DataFrame named
order_data. The DataFrame has columns for customer ID, order date, product name, and order quantity.
Your task is to analyze the data and answer specific questions about the orders.
Question: Using Pandas DataFrame operations, how would you find the following information from
the order_data DataFrame:
1. The total number of orders made by each customer.
2. The average order quantity for each product.
3. The earliest and latest order dates in the dataset.

import pandas as pd
order_data = pd.DataFrame({
    "Customer_ID": [101, 102, 101, 103, 102, 101],
    "Order_Date": ["2026-01-05", "2026-01-07", "2026-01-10",
                   "2026-01-12", "2026-01-15", "2026-01-20"],
    "Product_Name": ["Laptop", "Mouse", "Laptop",
                     "Keyboard", "Mouse", "Monitor"],
    "Order_Quantity": [2, 5, 1, 3, 4, 2]
})

order_data["Order_Date"] = pd.to_datetime(order_data["Order_Date"])

print("Total Orders by Customer")
print(order_data.groupby("Customer_ID").size())

print("\nAverage Order Quantity for Each Product")
print(order_data.groupby("Product_Name")["Order_Quantity"].mean())

print("\nEarliest Order Date")
print(order_data["Order_Date"].min())

print("\nLatest Order Date")
print(order_data["Order_Date"].max())
