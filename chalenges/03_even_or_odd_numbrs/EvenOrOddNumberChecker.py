#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Iker11111
# Created:     15-Aug-2018
# Updated:     15-Aug-2018
#-----------------------------------------------------------------------------

# Ask the user to input a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")