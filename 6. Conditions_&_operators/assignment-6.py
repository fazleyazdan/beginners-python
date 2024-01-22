# Alien Colors #1: Imagine an alien was just shot down in a game. 
# Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# • Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
# • Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

alien_color = 'green'
if alien_color == 'green':
    print("the player earned 5 points")

alien_color1 = 'blue'
if alien_color1 == 'green':
    print("nothing")
    

# Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
# • If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# • Write one version of this program that runs the if block and another that runs the else block.

alien_color2 = 'green'

if alien_color2 == 'green':
    print("the player earned 5 points")
else:
    print("the player earned 10 points")

if alien_color2 == 'red':
    print("the player earned 10 points")
else:
    print("the else block passed")
    

# Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.

alien_color3 = 'yellow'

if alien_color3 == 'green':
    print("the player earned 5 points")
elif alien_color3 == 'yellow':
    print("the player earned 10 points")
else:
    print("the player earned 15 points")


# Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
# • If the person is less than 2 years old, print a message that the person is a baby.
# • If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# • If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# • If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# • If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# • If the person is age 65 or older, print a message that the person is an elder

age = 27

if age < 2:
    print("the person is baby")
elif age >= 2 and age < 4:
    print("the person is toddler")
elif age >= 4 and age < 13:
    print("the person is a kid")
elif age >= 13 and age < 20:
    print("the person is a teenager")
elif age >= 20 and age < 65:
    print("the person is an adult")
else:
    print("the person is elder")
    

# Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
# • Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit is in your list. 
# If the fruit is in your list, the if block should print a statement, such as You really like bananas!


fav_fruits = ['bananas', 'pomegranate', 'grapes']

if 'bananas' in fav_fruits:
    print("\nyou really like bananas!")
if 'grapes' in fav_fruits:
    print("you really like grapes!")
if 'pomegranate' in fav_fruits:
    print("you really like pomegranate!")
if 'strawberry' in fav_fruits:
    print("you really like strawberry!")
if 'oranges' in fav_fruits:
    print("you really like oranges!")
  
  
