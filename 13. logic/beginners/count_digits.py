# Count the Number of Digits
# Problem: Write a Python function that takes an integer as input and counts the number of digits in it.
# Input: An integer n.
# Output: The number of digits in the integer


def count_digits(integer):
    str_integer = str(integer)        # as int obj has not 'len' method so we converted it to string
    count = len(str_integer)
    return count

print(count_digits(231235))           # output : 6

# alternative you can convert the int to string then apply loop on it, and increment the counter for each iteration.

