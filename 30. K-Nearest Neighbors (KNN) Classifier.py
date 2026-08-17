import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X = np.array([
    [1, 2], [2, 3], [1, 1], [3, 4],
    [4, 3], [5, 5], [4, 4], [5, 4]
])

y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

k = int(input("Enter K: "))

model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

s1 = float(input("Enter Symptom 1: "))
s2 = float(input("Enter Symptom 2: "))

prediction = model.predict([[s1, s2]])

if prediction[0] == 1:
    print("Patient has the condition")
else:
    print("Patient does not have the condition")
