
available_toppings = ['olives', 'mushroom', 'pepperoni', 'onions', 'nuggets', 'extra cheese']

requested_toppings = ['olives', 'mushroom', 'pepperoni']

for requseted_topping in requested_toppings:
    if requseted_topping in available_toppings:
        print(f"adding {requseted_topping} to your pizza")
    else:
        print("requested toppings are not available")

print("\nYour pizza is ready to eat")