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
