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
