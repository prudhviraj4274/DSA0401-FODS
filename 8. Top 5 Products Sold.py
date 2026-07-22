8. Scenario: You are a data scientist working for a company that sells products online. You have been
tasked with analyzing the sales data for the past month. The data is stored in a Pandas data frame.
Question: How would you find the top 5 products that have been sold the most in the past month?

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
