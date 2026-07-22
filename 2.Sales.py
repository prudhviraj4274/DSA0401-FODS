2. Scenario: You are a data analyst working for a company that sells products online. You have been
tasked with analyzing the sales data for the past month. The data is stored in a NumPy array.
Question: How would you find the average price of all the products sold in the past month? Assume
3x3 matrix with each row representing the sales for a different product

import numpy as np
sales = np.array([
    [100, 120, 110],
    [200, 210, 220],
    [150, 160, 170]
])
average_price = np.mean(sales)
print("Sales Matrix:")
print(sales)
print("\nAverage Price of All Products Sold:", average_price)
