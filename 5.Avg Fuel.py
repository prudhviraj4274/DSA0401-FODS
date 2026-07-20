import numpy as np
fuel_efficiency = np.array([25, 30, 35, 40])
average = np.mean(fuel_efficiency)
improvement = ((fuel_efficiency[3] - fuel_efficiency[0]) / fuel_efficiency[0]) * 100
print("Average Fuel Efficiency:", average)
print("Percentage Improvement:", improvement, "%")
