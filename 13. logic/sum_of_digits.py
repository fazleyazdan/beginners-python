# Problem: Write a Python function that takes an integer as input and returns the sum of its digits.
# Input: An integer n.
# Output: An integer representing the sum of the digits of n


def sum_of_digits(num):
    sum = 0                    # Initialize sum to 0
    str_num = str(num)         # Convert the integer to a string to iterate over each digit
    for digit in str_num:      # Iterate over each character in the string
        sum += int(digit)      # Convert the character back to an integer and add it to the sum
    return sum                 # return total_sum 

print(sum_of_digits(43))       # Output 7

    