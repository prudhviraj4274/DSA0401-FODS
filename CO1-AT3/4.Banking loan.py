import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/4 SLOT/FODS/AT 3/banking_loan.csv")

print("Banking Loan Approval Dataset")
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
print(data[["Income","Credit_Score","Loan_Amount"]].mean())

print("\nMedian")
print(data[["Income","Credit_Score","Loan_Amount"]].median())

print("\nMinimum")
print(data[["Income","Credit_Score","Loan_Amount"]].min())

print("\nMaximum")
print(data[["Income","Credit_Score","Loan_Amount"]].max())

print("\nStandard Deviation")
print(data[["Income","Credit_Score","Loan_Amount"]].std())

print("\nLoan Status Count")
print(data["Loan_Status"].value_counts())

print("\nCorrelation Matrix")
print(data[["Income","Credit_Score","Loan_Amount"]].corr())

plt.figure(figsize=(5,4))
plt.hist(data["Income"], bins=5)
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Customers")
plt.show()

plt.figure(figsize=(5,4))
plt.hist(data["Credit_Score"], bins=5)
plt.title("Credit Score Distribution")
plt.xlabel("Credit Score")
plt.ylabel("Customers")
plt.show()

plt.figure(figsize=(5,4))
data["Loan_Status"].value_counts().plot(kind="bar")
plt.title("Loan Approval Status")
plt.xlabel("Loan Status")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(5,4))
plt.scatter(data["Credit_Score"], data["Loan_Amount"])
plt.title("Credit Score vs Loan Amount")
plt.xlabel("Credit Score")
plt.ylabel("Loan Amount")
plt.show()

plt.figure(figsize=(6,4))
data.boxplot(column=["Income","Credit_Score","Loan_Amount"])
plt.title("Box Plot")
plt.show()
