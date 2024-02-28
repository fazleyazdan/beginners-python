# Task 1 : Deli
# Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches. 
# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
# As each sandwich is made, move it to the list of finished sandwiches. 
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['chicken sandwitch', 'egg sandwitch', 'beef sandwitch']
finished_sandwiches = []

while sandwich_orders:
    (sandwich_orders)
    order = sandwich_orders.pop()
    print(f"i made your {order}")
    finished_sandwiches.append(order)

print(f"\nready to eat sandwiches")
for finished in finished_sandwiches:
    print(f"\t{finished}")