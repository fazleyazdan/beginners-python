# Write a function: which returns true, when passed a number to it and is completely divisible by 3.

def divisble_by_three(num):
    if num % 3 == 0:
        return True
    else:
        return False
    
print(divisble_by_three(6))     #! True
print(divisble_by_three(8))     #! False
