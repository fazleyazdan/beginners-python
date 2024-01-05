

# 1. value**2: This is the expression used to calculate the square of each value in the range.

# 2. range(1, 11): This creates an iterable that includes the numbers from 1 to 10 (inclusive).

# 3. [value**2 for value in range(1, 11)]: This is a list comprehension that iterates over the numbers from 1 to 10, 

# 4. calculates the square of each number, and creates a new list (squares) containing these squared values.

squares = [value**2 for value in range(1,11)]

print(squares)
