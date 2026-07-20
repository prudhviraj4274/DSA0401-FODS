import numpy as np
prices = np.array([100, 200, 50, 80])
quantities = np.array([2, 1, 4, 3])
discount_rate = 10
tax_rate = 5
total = np.sum(prices * quantities)
discount = total * discount_rate / 100
tax = (total - discount) * tax_rate / 100
final_amount = total - discount + tax
print("Total Cost:", total)
print("Discount:", discount)
print("Tax:", tax)
print("Final Amount:", final_amount)
