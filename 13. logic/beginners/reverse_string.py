# Reverse a String:
# Problem: Write a Python function that takes a string as input and returns the string reversed.
# Input: A string s.
# Output: The reversed string.


def reverse_string(string):
    size = len(string)
    rev_string = ""
    for i in reversed(string):
        rev_string += i
    return rev_string        

print(reverse_string("asd"))
    
    
    
#! we can also do it through slicing method

def reverse_string_2(s):
    rev_string = s[::-1]
    return rev_string

print(f"Method 2: {reverse_string('asdf')}")