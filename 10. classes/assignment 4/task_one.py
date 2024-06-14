# Dice: Make a class Die with one attribute called sides, which has a default value of 6. 
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
# Make a 6-sided die and roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint


class Die:
    
    def __init__(self, sides = 0):
        self.sides = sides
        
    def roll_die(self):
        roll_num = randint(1, self.sides)
        print(roll_num, end= "  ")
        
six_die = Die(6)
ten_die = Die(10)
twenty_die = Die(20)

print("rolling six sided die 10 times:")
for count in range(1,11):
    six_die.roll_die()
    count += count

print("\nrolling 10 sided die 10 times:")
for count in range(1,11):
    ten_die.roll_die()
    count += count
    
print("\nrolling 20 sided die 10 times:")
for count in range(1,11):
    twenty_die.roll_die()
    count += count