import pandas as pd

sales_data = pd.DataFrame({
    "Age":[22,25,22,30,25,25,35,22,30,40]
})

frequency = sales_data["Age"].value_counts()

print(frequency)
