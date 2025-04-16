# Program Name: Sum of Numbers
# Purpose: This program takes a number 'n' from the user and calculates the sum of all numbers from 1 to 'n' using a for loop.
# Creator: iker
# Student Number: 1013130
# Date: March 26

# We will ask the user for a number 'n' and then calculate the sum of all numbers from 1 to 'n'.

# Step 1: Ask the user to enter a number
import time

print("Welcome to the Sum of Numbers program!")
n = int(input(
    "Please enter a positive integer 'n' to calculate the sum of all numbers from 1 to 'n': "))  # Convert input to an integer


start_time = time.perf_counter()

# Step 2: Check if the number is valid
if n <= 0:
    print("Sorry, the number must be greater than 0. Please restart the program and enter a valid number.")
else:
    # Step 3: Initialize a variable to store the sum
    sum_of_numbers = 0  # This variable will store the sum of numbers

    print(f"\nLet's calculate the sum of all numbers from 1 to {n}.")

    # Step 4: Use a for loop to add numbers from 1 to 'n'
    for i in range(1, n + 1):  # Loop from 1 to n
        sum_of_numbers += i  # Add the current number to the sum
        print(f"Adding {i}: Current sum is {sum_of_numbers}")  # Show the current step

    # Step 5: Display the result
    print(f"\nThe total sum of all numbers from 1 to {n} is {sum_of_numbers}.")  # Output the final sum

end_time = time.perf_counter()

print(f"\nExecution time: {end_time - start_time:.4f} seconds")