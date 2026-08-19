12. Scenario: You are working on a data analysis project that involves analyzing the monthly
temperature and rainfall data for a city. You have a dataset containing the monthly temperature and
rainfall values for each month of a year. Your task is to develop a Python program that generates line
plots and scatter plots to visualize the temperature and rainfall data.
Question:
1. Develop a Python program to create a line plot of the monthly temperature data.
2: Develop a Python program to create a scatter plot of the monthly rainfall data.

import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun"]
temperature = [25,27,30,34,36,38]
rainfall = [20,15,30,45,80,120]

plt.plot(months, temperature, marker='o')
plt.title("Monthly Temperature")
plt.xlabel("Months")
plt.ylabel("Temperature")
plt.show()

plt.scatter(months, rainfall)
plt.title("Monthly Rainfall")
plt.xlabel("Months")
plt.ylabel("Rainfall")
plt.show()
