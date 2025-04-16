# Original list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List of even numbers using list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]

# List of squares of the even numbers
squared_numbers = [num ** 2 for num in even_numbers]

# Print the results
print("even_numbers =", even_numbers)
print("squared_numbers =", squared_numbers)
