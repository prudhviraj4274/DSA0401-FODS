import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/4 SLOT/FODS/AT 3/retail_sales.csv")

print("Retail Sales Dataset")
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
print(data[["Price","Quantity_Sold","Discount","Revenue"]].mean())

print("\nMedian")
print(data[["Price","Quantity_Sold","Discount","Revenue"]].median())

print("\nMinimum")
print(data[["Price","Quantity_Sold","Discount","Revenue"]].min())

print("\nMaximum")
print(data[["Price","Quantity_Sold","Discount","Revenue"]].max())

print("\nStandard Deviation")
print(data[["Price","Quantity_Sold","Discount","Revenue"]].std())

print("\nCategory Count")
print(data["Category"].value_counts())

print("\nCorrelation Matrix")
print(data[["Price","Quantity_Sold","Discount","Revenue"]].corr())

plt.figure(figsize=(5,4))
plt.hist(data["Revenue"], bins=5)
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Products")
plt.show()

plt.figure(figsize=(5,4))
plt.hist(data["Quantity_Sold"], bins=5)
plt.title("Quantity Sold Distribution")
plt.xlabel("Quantity Sold")
plt.ylabel("Products")
plt.show()

plt.figure(figsize=(5,4))
data["Category"].value_counts().plot(kind="bar")
plt.title("Product Categories")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(5,4))
plt.scatter(data["Price"], data["Revenue"])
plt.title("Price vs Revenue")
plt.xlabel("Price")
plt.ylabel("Revenue")
plt.show()

plt.figure(figsize=(6,4))
data.boxplot(column=["Price","Quantity_Sold","Discount","Revenue"])
plt.title("Box Plot")
plt.show()
