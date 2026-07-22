6. Scenario: You are a cashier at a grocery store and need to calculate the total cost of a customer's
purchase, including applicable discounts and taxes. You have the item prices and quantities in separate
lists, and the discount and tax rates are given as percentages. Your task is to calculate the total cost for
the customer.
Question: Use arithmetic operations to calculate the total cost of a customer's purchase, including
discounts and taxes, given the item prices, quantities, discount rate, and tax rate?
                                                                                                        
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
