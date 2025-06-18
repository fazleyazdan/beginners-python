# write a function , which takes 3 or 4. when it takes 3 it return 4. and when it takes 4 it return 3. 
#! Note : don't use conditions or any built in method

def rotate_three_four(num):
    dict = {3:4 , 4:3}
    return dict[num]

num = rotate_three_four(4)
num1 = rotate_three_four(3)
print(num)
print(num1)


#! ======= OR =======

print("\n***** Another Approach *****")

def switch_three_four(x):
    return {3: 4, 4: 3}[x]

# Testing the function
print(switch_three_four(3))  # Output: 4
print(switch_three_four(4))  # Output: 3



# When you use [x] after the dictionary, you are accessing the value associated with the key x in that dictionary.

#* Example
# If x is 3, {3: 4, 4: 3}[3] will return 4 because the key 3 maps to the value 4 in the dictionary.
# If x is 4, {3: 4, 4: 3}[4] will return 3 because the key 4 maps to the value 3 in the dictionary.

#* Why Use [x]?
# The [x] syntax is how you access values in a dictionary in Python. Here's how it works step-by-step:

#* Dictionary Creation: {3: 4, 4: 3}

# This is a dictionary with keys 3 and 4.
# Accessing a Value: {3: 4, 4: 3}[x]

#* When you place [x] after the dictionary, you're asking for the value associated with the key x.

