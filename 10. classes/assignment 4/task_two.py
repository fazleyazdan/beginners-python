

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

