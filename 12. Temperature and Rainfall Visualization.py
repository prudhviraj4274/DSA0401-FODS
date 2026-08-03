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
