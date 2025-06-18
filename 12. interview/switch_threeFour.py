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





