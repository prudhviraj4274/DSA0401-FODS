9. Scenario: You work for a real estate agency and have been given a dataset containing information
about properties for sale. The dataset is stored in a Pandas DataFrame named property_data. The
DataFrame has columns for property ID, location, number of bedrooms, area in square feet, and listing
price. Your task is to analyze the data and answer specific questions about the properties.
Question: Using Pandas DataFrame operations, how would you find the following information from
the property_data DataFrame:
1. The average listing price of properties in each location.
2. The number of properties with more than four bedrooms.
3. The property with the largest area.
    
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
