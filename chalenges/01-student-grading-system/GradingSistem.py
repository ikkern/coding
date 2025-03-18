
#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Iker11111
# Created:     15-Aug-2018
# Updated:     15-Aug-2018
#-----------------------------------------------------------------------------


# Student gradinscore = int(input("Please enter your score (out of 100): "))
score = int(input("Please enter your score (out of 100): "))
# Grading
if score >= 90:
    print("greattt jobbb u got an: A")
elif 80 <= score <= 89:
    print("good jobbb you got a:  B")
elif 70 <= score <= 79:
    print("good work you got a: C")
elif 60 <= score <= 69:
    print(" do better next time you got a: D")
elif score < 60:
    print("do better next time F")
else:
    print("Invalid score provided.")
    print("Please enter a valid number!")
