import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/4 SLOT/FODS/AT 3/agriculture_crop_yield.csv")

print("Agriculture Crop Yield Dataset")
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
print(data[["Rainfall_mm","Temperature","Fertilizer_kg","Crop_Yield_kg"]].mean())

print("\nMedian")
print(data[["Rainfall_mm","Temperature","Fertilizer_kg","Crop_Yield_kg"]].median())

print("\nMinimum")
print(data[["Rainfall_mm","Temperature","Fertilizer_kg","Crop_Yield_kg"]].min())

print("\nMaximum")
print(data[["Rainfall_mm","Temperature","Fertilizer_kg","Crop_Yield_kg"]].max())

print("\nStandard Deviation")
print(data[["Rainfall_mm","Temperature","Fertilizer_kg","Crop_Yield_kg"]].std())

print("\nSoil Type Count")
print(data["Soil_Type"].value_counts())

print("\nCorrelation Matrix")
print(data[["Rainfall_mm","Temperature","Fertilizer_kg","Crop_Yield_kg"]].corr())

plt.figure(figsize=(5,4))
plt.hist(data["Crop_Yield_kg"], bins=5)
plt.title("Crop Yield Distribution")
plt.xlabel("Crop Yield (kg)")
plt.ylabel("Farms")
plt.show()

plt.figure(figsize=(5,4))
plt.hist(data["Rainfall_mm"], bins=5)
plt.title("Rainfall Distribution")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Farms")
plt.show()

plt.figure(figsize=(5,4))
data["Soil_Type"].value_counts().plot(kind="bar")
plt.title("Soil Type")
plt.xlabel("Soil Type")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(5,4))
plt.scatter(data["Fertilizer_kg"], data["Crop_Yield_kg"])
plt.title("Fertilizer vs Crop Yield")
plt.xlabel("Fertilizer (kg)")
plt.ylabel("Crop Yield (kg)")
plt.show()

plt.figure(figsize=(6,4))
data.boxplot(column=["Rainfall_mm","Temperature","Fertilizer_kg","Crop_Yield_kg"])
plt.title("Box Plot")
plt.show()
