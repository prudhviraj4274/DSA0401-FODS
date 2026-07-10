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
