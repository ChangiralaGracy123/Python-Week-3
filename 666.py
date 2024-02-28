# Filename: 666.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program that prompts the user to enter a number in the range 1 to 100 and validates the input
# Last changed: 12-02-2024

# Program that prompts the user to enter a number in the range 1 to 100 and validates the input

# Initialize an empty list to store the entered numbers
x = []

# Keep prompting the user until they enter 666 to exit
while x != 666:
    # Prompt the user to enter a number
    x = int(input("Enter a number between 1 and 100 (inclusive), or 666 to exit: "))
    # Check if the user wants to exit
    if x == 666:
        print("Exiting...")
        break
    # Check if the entered number is out of range
    elif x < 1 or x > 100:
        print("Number out of range. Please try again.")
    # If the number is within the valid range, add it to the list
    else:
        print("Valid number entered:", x)

# Description:
# This code continuously prompts the user to enter a number between 1 and 100 (inclusive) until they enter 666 to exit.
# If the user enters a number outside this range, it prompts them to try again.
# If the number is within the valid range, it prints that it's a valid number and adds it to the list.