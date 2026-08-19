11. Scenario : You are a data scientist working for a company that sells products online. You have
been tasked with creating a simple plot to show the sales of a product over time.

Question:
1. Write code to create a simple line plot in Python using Matplotlib to predict sales happened in a
month?
2. Write code to create a scatter plot in Python using Matplotlib to predict sales happened in a month?
3. Develop a Python program to create a bar plot of the monthly sales data.

import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun"]
sales = [100,150,200,180,250,300]

plt.plot(months, sales, marker='o')
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

plt.scatter(months, sales)
plt.title("Monthly Sales - Scatter Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

plt.bar(months, sales)
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
