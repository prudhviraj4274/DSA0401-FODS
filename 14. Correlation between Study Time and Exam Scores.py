import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Study_Time":[1,2,3,4,5,6],
    "Score":[40,50,60,70,80,90]
})

correlation = data["Study_Time"].corr(data["Score"])

print("Correlation:", correlation)

plt.scatter(data["Study_Time"], data["Score"])
plt.title("Study Time vs Exam Score")
plt.xlabel("Study Time")
plt.ylabel("Score")
plt.show()
