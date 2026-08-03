import pandas as pd

data = pd.DataFrame({
    "City":["Chennai","Bangalore","Hyderabad"],
    "Mean":[34,28,31],
    "Std":[2.5,1.2,3.1],
    "Highest":[38,30,36],
    "Lowest":[30,26,27]
})

data["Range"] = data["Highest"] - data["Lowest"]

print("Mean Temperature")
print(data[["City","Mean"]])

print("\nStandard Deviation")
print(data[["City","Std"]])

print("\nCity with Highest Temperature Range")
print(data.loc[data["Range"].idxmax()])

print("\nMost Consistent Temperature")
print(data.loc[data["Std"].idxmin()])
