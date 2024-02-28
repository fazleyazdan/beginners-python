# Task 1 : Deli
# Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches. 
# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
# As each sandwich is made, move it to the list of finished sandwiches. 
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['chicken', 'egg', 'beef']
finished_sandwiches = []

while sandwich_orders:
    sandwich_orders.reverse()
    order = sandwich_orders.pop()
    print(f"i made your {order} sandwich")
    finished_sandwiches.append(order)

print(f"\nready to eat sandwiches")
for finished in finished_sandwiches:
    print(f"\t{finished} sandwich")
    
    
#! Task 2 : No Pastrami 
# Using the list sandwich_orders, make sure the sandwich 'pastrami' appears in the list at least three times. 
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
# Make sure no pastrami sandwiches end up in finished_sandwiches

print("==================================================================")
sandwich_orders = ['pastrami','chicken', 'pastrami','egg','pastrami', 'beef']
print("\noh No! our restaurant has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    sandwich_orders.reverse()
    order = sandwich_orders.pop()
    print(f"i made your {order} sandwich")
    finished_sandwiches.append(order)

print(f"\nready to eat sandwiches")
for finished in finished_sandwiches:
    print(f"\t{finished} sandwich")
    
    
#! Task 3: Dream Vacation 
# Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world, where would you go? 
# Include a block of code that prints the results of the poll

print("==================================================================")
dream_vacation = {}
flag = True

while flag:
    name = input("\nEnter your name: ")
    dream_place = input("\nIf you could visit one place in the world, where would you go? ")
    dream_vacation[name] = dream_place
    response = input("\nwanna take another poll? type 'yes/no': ")
    if response == 'no':
        flag = False

print("\n*** Results of poll are as follows:\n")
for key, val in dream_vacation.items():
    print(f"\t{key.title()} : {val.title()}")