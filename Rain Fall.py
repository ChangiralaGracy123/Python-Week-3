# Filename: Rain Fall.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program that calculates the average monthly rainfall of the year
# Last changed: 12-02-2024

# Calculating total rainfall for the year, average monthly rainfall, and identifying months with the highest and lowest rainfall

# Initialize a list to hold the names of the months
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# Initialize an empty list to hold the rainfall totals for each month
rainfall_totals = []

# Loop to input rainfall for each month
index = 0
while index < len(months):
    rainfall = float(input(f"Enter total rainfall for {months[index]} (in inches): "))
    rainfall_totals.append(rainfall)
    index += 1

# Calculate total rainfall for the year
total_rainfall = sum(rainfall_totals)

# Calculate average monthly rainfall
average_rainfall = total_rainfall / len(months)

# Find the month with the highest and lowest rainfall
max_rainfall = max(rainfall_totals)
min_rainfall = min(rainfall_totals)
max_month = months[rainfall_totals.index(max_rainfall)]
min_month = months[rainfall_totals.index(min_rainfall)]

# Display the results
print("\nTotal rainfall for the year:", total_rainfall, "inches")
print("Average monthly rainfall:", average_rainfall, "inches")
print("Month with the highest rainfall:", max_month, "with", max_rainfall, "inches")
print("Month with the lowest rainfall:", min_month, "with", min_rainfall, "inches")

# Description:
# We initialize a tuple months to hold the names of the months.
# We initialize an empty list rainfall_totals to hold the rainfall totals for each month.
# Using a while loop, we prompt the user to input the total rainfall for each month, and we append each input to the rainfall_totals list.
# We calculate the total rainfall for the year by summing up all the values in rainfall_totals.
# We calculate the average monthly rainfall by dividing the total rainfall by the number of months.
# We find the month with the highest rainfall and the month with the lowest rainfall using the max() and min() functions respectively, and we retrieve the corresponding month names using indexing.
# Finally, we display the total rainfall for the year, the average monthly rainfall, and the months with the highest and lowest rainfall.
