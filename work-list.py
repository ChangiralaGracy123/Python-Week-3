# Filename: work-list.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program that adds one more integer to a List of six integers
# Last changed: 12-02-2024

# Program that adds one more integer to a List of six integers

# List of six integers
numbers = [2, 4, 6, 8, 10, 12]

# Use a list method to add one more integer
numbers.append(8)

# Use a list method to sort the list
numbers.sort()

# Use a While Loop to print the entries

# Initialize index for while loop
index = 0

# While loop to print each element of the list
while index < len(numbers):
    # Print the current element at index position
    print(numbers[index])
    # Increment index to move to the next element
    index += 1

# Description:
# The code starts with a list numbers containing six integers.
# It appends one more integer (8) to the list using the append() method.
# The list is then sorted in ascending order using the sort() method.
# A while loop is used to iterate over the list and print each element.
# The index variable is initialized to 0 to keep track of the current position in the list.
# Inside the while loop, each element of the list is printed using the current index (numbers[index]).
# After printing, the index is incremented by 1 to move to the next element in the list.
# The loop continues until the index becomes equal to the length of the numbers list.