import numpy as np
house_data = np.array([
    [3, 1200, 250000],
    [5, 1800, 450000],
    [4, 1500, 350000],
    [6, 2200, 550000],
    [5, 2000, 500000]
])
houses = house_data[house_data[:, 0] > 4]
average_price = np.mean(houses[:, 2])
print("Average Sale Price:", average_price)
