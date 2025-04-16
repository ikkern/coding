# List Comprehensions and Filtering

This Python code structure demonstrates how to use list comprehension to extract even numbers from a list and then square those numbers. The process is broken down into three steps:

1. Extract even numbers from a given list of integers.
2. Square each of the even numbers.
3. Print the results.

## Code Explanation

```python
# Original list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List of even numbers using list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]

# List of squares of the even numbers
squared_numbers = [num ** 2 for num in even_numbers]

# Print the results
print("even_numbers =", even_numbers)
print("squared_numbers =", squared_numbers)