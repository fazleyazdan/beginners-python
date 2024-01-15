

# 1. value**2: This is the expression used to calculate the square of each value in the range.

# 2. range(1, 11): This creates an iterable that includes the numbers from 1 to 10 (inclusive).

# 3. [value**2 for value in range(1, 11)]: This is a list comprehension that iterates over the numbers from 1 to 10, 

# 4. calculates the square of each number, and creates a new list (squares) containing these squared values.

squares = [value**2 for value in range(1,11)]

print(squares)


# To use this syntax, begin with a descriptive name for the list, such as 
# squares. Next, open a set of square brackets and define the expression for 
# the values you want to store in the new list. In this example the expression is 
# value**2, which raises the value to the second power. Then, write a for loop 
# to generate the numbers you want to feed into the expression, and close the 
# square brackets. The for loop in this example is for value in range(1, 11), 
# which feeds the values 1 through 10 into the expression value**2. Note that 
# no colon is used at the end of the for statement.

# simple methode of squares

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# another methode

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)
