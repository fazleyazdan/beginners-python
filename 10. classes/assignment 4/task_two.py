#  Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. 
# Randomly select 4 numbers or letters from the list and print a message saying that 
# any ticket matching these 4 numbers or letters wins a prize.

from random import choice

lottery = [1,2,3,4,5,6,7,8,9,10,'a', 'b', 'c', 'd', 'e', 'f']
prize_numbers = []


#* i have added extra functionality. if the random number is selected twice then i have to remove it from the lottery to not be selected again

for _ in range(4):
    num = choice(lottery)
    prize_numbers.append(num)
    lottery.remove(num)
    
print("Silent Please: any ticket matching the below number or letters have won the prize")
print(prize_numbers)


""" In Python, the underscore (_) is often used as a throwaway variable. 
It is a convention used to indicate that the variable is temporary and its value is not important or will not be used.
This is particularly useful in loops where the loop variable itself is not needed inside the loop body."""