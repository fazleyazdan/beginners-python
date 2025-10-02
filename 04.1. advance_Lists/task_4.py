# Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

for value in range(1,21):
    print(value)
    
#  Make a list of the numbers from one to one million, and then 
# use a for loop to print the numbers. (If the output is taking too long, stop it by 
# pressing CTRL-C or by closing the output window.)

million = list(range(1,10**6))
# for value in million:
    # print(value)


# Make a list of the numbers from one to one million, and 
# then use min() and max() to make sure your list actually starts at one and ends 
# at one million. Also, use the sum() function to see how quickly Python can add a million numbers

print("min in a million :",min(million))
print("max in a million :",max(million))
print("adding a million :",sum(million))  

# Use the third argument of the range() function to make a list 
# of the odd numbers from 1 to 20. Use a for loop to print each number

odd_number = list(range(1,20,2))
print("odd number from 1 to 20 :", odd_number)

# Make a list of the multiples of 3, from 3 to 30. Use a for loop to 
# print the numbers in your list.

multiple_3 = [value*3 for value in range(1,11)]            # list comprehension
for multiple in multiple_3:
    print(multiple)
    
# A number raised to the third power is called a cube. For example, 
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes 
# (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube

cubes = []

for value in range(1,11):
    cube = value**3
    cubes.append(cube)
    print(cube)
    
# Use a list comprehension to generate a list of the first 10 cubes.

cubes_comprehension = [value**3 for value in range(1,11)]
print(cubes_comprehension)