import pandas as pd

property_data = pd.DataFrame({
    "Property_ID": [1, 2, 3, 4, 5],
    "Location": ["Chennai", "Chennai", "Bangalore", "Hyderabad", "Bangalore"],
    "Bedrooms": [3, 5, 4, 6, 5],
    "Area": [1200, 2200, 1800, 3000, 2500],
    "Listing_Price": [5000000, 8500000, 7000000, 12000000, 9500000]
})

print("Average Listing Price")
print(property_data.groupby("Location")["Listing_Price"].mean())

print("\nProperties with More than 4 Bedrooms")
print(len(property_data[property_data["Bedrooms"] > 4]))

print("\nProperty with Largest Area")
print(property_data.loc[property_data["Area"].idxmax()])
