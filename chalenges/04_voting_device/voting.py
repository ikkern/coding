#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Iker11111
# Created:     15-Aug-2018
# Updated:     15-Aug-2018
#-----------------------------------------------------------------------------

# Program to check voting eligibility

# Ask the user to enter their age
age = int(input("Enter your age: "))

# Check eligibility using conditional statements
if age >= 18:
    print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible to vote yet.")