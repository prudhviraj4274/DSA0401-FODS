15. Scenario: You work for a weather data analysis company, and your team is responsible for
developing a program to calculate and analyze variability in temperature data for different cities.
Question: Write a python program will take in a dataset containing daily temperature readings for each
city over a year and perform the following tasks:
1. Calculate the mean temperature for each city.
2. Calculate the standard deviation of temperature for each city.
3. Determine the city with the highest temperature range (difference between the highest and lowest
temperatures).
4. Find the city with the most consistent temperature (the lowest standard deviation).
                                 
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
