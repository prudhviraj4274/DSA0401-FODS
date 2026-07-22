10. Scenario: You are working on a data visualization project and need to create basic plots using
Matplotlib. You have a dataset containing the monthly sales data for a company, including the month
and corresponding sales values. Your task is to develop a Python program that generates line plots and
bar plots to visualize the sales data.
Question:
1. How would you develop a Python program to create a line plot of the monthly sales data?
2: How would you develop a Python program to create a bar plot of the monthly sales data?

import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [2000, 2500, 3000, 2800, 3500, 4000]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

plt.bar(months, sales)
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
