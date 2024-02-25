# When you use the input() function, Python interprets everything the user enters as a string.
# We can resolve this issue by using the int() function, which converts the input string to a numerical value.
# Using int() to Accept Numerical Input

print("\n**** Approach 1 ****\n")
age = input("Enter you age please: ")

# if age >= 18:                     #! this will give an error because the input is taken as string. convert it to int
if int(age) >= 18:
    print(f"Your age is {age}, you can vote")         
else:
    print(f"Your age is {age}, you can't vote")         

#* ============================================== #

print("\n**** Approach 2 ****\n")

height = input("how tall are you? ")
height = int(height)

if height >= 48:
    print("You can ride a roller coster")
else:
    print("You can't ride a roller coster")
    