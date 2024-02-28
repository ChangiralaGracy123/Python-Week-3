# Filename: Salary.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program that calculates the salary over a period of time doubling each day
# Last changed: 12-02-2024

# Program that calculates the salary over a period of time doubling each day

# Initialize an empty list to store the salary for each day
salaries = []

# Ask the user for the number of days
num_days = int(input("Enter the number of days: "))

total_pay = 0

print("Day\tSalary")
print("-" * 15)

# Calculate the salary for each day and store it in the list
for day in range(1, num_days + 1):
    # Calculate the salary for the current day (in dollars)
    salary = 2 ** (day - 1) / 100
    # Add the salary for the current day to the total pay
    total_pay += salary
    # Add the salary for the current day to the list
    salaries.append(salary)
    print(f"{day}\t${salary:.2f}")

# Display the total pay at the end of the period
print("\nTotal pay over", num_days, "days: $", total_pay)

# Description:
# We initialize an empty list salaries to store the salary for each day.
# We ask the user for the number of days.
# We then calculate the salary for each day using the formula 2 ** (day - 1) / 100, where day represents the current day.
# We add each day's salary to the salaries list and also add it to the total_pay.
# Finally, we display a table showing the salary for each day and the total pay at the end of the period.