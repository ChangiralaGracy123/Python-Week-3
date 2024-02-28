# Filename: calculate_sales.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program that calculates Weekly Sales
# Last changed: 12-02-2024

# Program that calculates Weekly Sales

# Ask the user to enter a store's sales for each day of the week
sales = []
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Iterate through each day of the week
for day in days_of_week:
    # Prompt the user to enter the sales for the current day and convert it to float
    sales.append(float(input(f"Enter sales for {day}: ")))

# Use a loop to calculate the total sales for the week
total_sales = sum(sales)

# Display the total sales for the week
print("Total sales for the week:", total_sales)

# Description:
# The program first initializes an empty list sales to store the sales amounts for each day of the week.
# It iterates through each day of the week using a for loop.
# For each day, it prompts the user to enter the sales amount for that day and converts it to a floating-point number using float().
# The sales amount for each day is appended to the sales list.
# After collecting all the sales data, it calculates the total sales for the week using the sum() function, which adds up all the elements in the sales list.
# Finally, it displays the total sales for the week using the print() function.

