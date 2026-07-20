import pandas as pd

sales_data = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor",
                "Mouse", "Laptop", "Mouse", "Monitor",
                "Keyboard", "Printer"],
    "Quantity": [5, 20, 10, 8, 15, 12, 10, 7, 6, 9]
})

top5 = sales_data.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(5)

print("Top 5 Products Sold")
print(top5)
