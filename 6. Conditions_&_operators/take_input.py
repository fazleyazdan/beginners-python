# i have converted user input into int because by defualt user input is taken in string ...
# And you can't compare a string with int. you have to convert it into int. you can also do it : if int(user_age) >= 18

user_age = int(input("enter your age please : "))

if user_age >= 18 :
    print("you can vote for your desired candidate")
    
else:
    print("you can't vote, your age is less than 18")
