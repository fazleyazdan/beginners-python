# Sum of First N Natural Numbers
# Problem: Write a Python function that takes an integer n as input and returns the sum of the first n natural numbers.
# Input: An integer n.
# Output: The sum of the first n natural numbers.


def sum_natural_numbers(n):
    
    natural_sum = 0              # for adding natural numbers
    change_num = 0               # for changing the natural numbers
    
    for i in range(n):
        change_num += 1
        natural_sum += change_num
    return natural_sum

print(sum_natural_numbers(4))


#! the optimized version
# we can exclude the 'change_num' 

def sum_natural_numbers1(n):
    
    sum = 0         
    for i in range(1, n+1):      #! why n+1 : Commentary Below
        sum += i
    return sum

