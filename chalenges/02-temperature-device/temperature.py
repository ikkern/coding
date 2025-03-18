#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Iker11111
# Created:     15-Aug-2018
# Updated:     15-Aug-2018
#-----------------------------------------------------------------------------

# Ask the user to input the current temperature
temperature = float(input("Enter the temperature in Celsius: "))

# Provide advice based on the temperature

# If the temperature is below 10°C, print: `"It's cold outside."`
if temperature < 10:
    print("It's cold outside.")
#If th temperature is below 25 but avobe 10 it will print "its a nice day"
elif 10 <= temperature <= 25:
    print("It's a nice day. ")
#If the temperature is above 25 ot will print " Its hot outside"
else:
    print("It's hot outside.")