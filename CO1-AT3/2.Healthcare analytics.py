import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/4 SLOT/FODS/AT 3/healthcare_analytics.csv")

print("Healthcare Analytics Dataset")
print(data)

print("\nRows and Columns")
print(data.shape)

print("\nData Types")
print(data.dtypes)

print("\nDataset Information")
print(data.info())

print("\nMissing Values")
print(data.isnull().sum())

print("\nDuplicate Values")
print(data.duplicated().sum())

print("\nStatistical Summary")
print(data.describe())

print("\nMean")
print(data[["Age","Sugar_Level","BP","BMI"]].mean())

print("\nMedian")
print(data[["Age","Sugar_Level","BP","BMI"]].median())

print("\nMinimum")
print(data[["Age","Sugar_Level","BP","BMI"]].min())

print("\nMaximum")
print(data[["Age","Sugar_Level","BP","BMI"]].max())

print("\nStandard Deviation")
print(data[["Age","Sugar_Level","BP","BMI"]].std())

print("\nDisease Status Count")
print(data["Disease_Status"].value_counts())

print("\nCorrelation Matrix")
print(data[["Age","Sugar_Level","BP","BMI"]].corr())

plt.figure(figsize=(5,4))
plt.hist(data["Sugar_Level"], bins=5)
plt.title("Sugar Level Distribution")
plt.xlabel("Sugar Level")
plt.ylabel("Patients")
plt.show()

plt.figure(figsize=(5,4))
plt.hist(data["BMI"], bins=5)
plt.title("BMI Distribution")
plt.xlabel("BMI")
plt.ylabel("Patients")
plt.show()

plt.figure(figsize=(5,4))
data["Disease_Status"].value_counts().plot(kind="bar")
plt.title("Disease Status")
plt.xlabel("Disease")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(5,4))
plt.scatter(data["Sugar_Level"], data["BMI"])
plt.title("Sugar Level vs BMI")
plt.xlabel("Sugar Level")
plt.ylabel("BMI")
plt.show()

plt.figure(figsize=(6,4))
data.boxplot(column=["Age","Sugar_Level","BP","BMI"])
plt.title("Box Plot")
plt.show()
