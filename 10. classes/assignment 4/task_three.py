# Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 
# Make a list or tuple called my_ticket. 
# Write a loop that keeps pulling numbers until your ticket wins. 
# Print a message reporting how many times the loop had to run to give you a winning ticket.

from random import choice

lottery = [1,2,3,4,5,6,7,8,9,10,'a', 'b', 'c', 'd', 'e', 'f']

prize_numbers = []
lucky_num = choice(lottery)
prize_numbers.append(lucky_num)
my_ticket = 7

count = 0

while my_ticket not in prize_numbers:
    
    count += 1
    lucky_num = choice(lottery)
    prize_numbers.append(lucky_num)    
    if my_ticket in prize_numbers:
        count += 1
        break   

print(f"Congrats! it took {count} times to win the ticket")
print(prize_numbers)
