import pandas as pd
from sklearn.tree import DecisionTreeRegressor

data = pd.DataFrame({
    "Mileage": [20000, 30000, 40000, 50000, 60000, 70000],
    "Age": [2, 3, 4, 5, 6, 7],
    "Brand": [1, 1, 2, 2, 3, 3],
    "Engine": [1, 2, 1, 2, 1, 2],
    "Price": [900000, 800000, 700000, 600000, 500000, 400000]
})

X = data[["Mileage", "Age", "Brand", "Engine"]]
y = data["Price"]

model = DecisionTreeRegressor(random_state=1)
model.fit(X, y)

mileage = float(input("Enter Mileage: "))
age = float(input("Enter Age: "))
brand = int(input("Enter Brand (1-3): "))
engine = int(input("Enter Engine (1-2): "))

price = model.predict([[mileage, age, brand, engine]])

print("Predicted Car Price:", round(price[0], 2))
