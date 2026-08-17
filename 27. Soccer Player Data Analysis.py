import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Name": ["Ravi", "Arun", "John", "David", "Sam",
             "Alex", "Vijay", "Ryan", "Kiran", "Mike"],
    "Age": [22, 25, 28, 30, 24, 27, 32, 21, 29, 26],
    "Position": ["Forward", "Midfielder", "Forward", "Defender",
                 "Goalkeeper", "Midfielder", "Defender",
                 "Forward", "Midfielder", "Forward"],
    "Goals": [20, 15, 25, 8, 2, 18, 10, 22, 16, 14],
    "Salary": [5000, 4500, 6000, 4000, 3500,
               5500, 4200, 4800, 5200, 4600]
})

# Save as CSV
data.to_csv("players.csv", index=False)

# Read CSV
df = pd.read_csv("players.csv")

print("Top 5 Players by Goals:")
print(df.nlargest(5, "Goals")[["Name", "Goals"]])

print("\nTop 5 Players by Salary:")
print(df.nlargest(5, "Salary")[["Name", "Salary"]])

average_age = df["Age"].mean()

print("\nAverage Age:", average_age)

print("\nPlayers Above Average Age:")
print(df[df["Age"] > average_age]["Name"])

# Position distribution
df["Position"].value_counts().plot(kind="bar")

plt.title("Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.show()
