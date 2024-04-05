'''If you want a function to accept several different kinds of arguments, the 
parameter that accepts an arbitrary number of arguments must be placed 
last in the function definition. Python matches positional and keyword 
arguments first and then collects any remaining arguments in the final 
parameter.
For example, if the function needs to take in a size for the pizza, that 
parameter must come before the parameter *toppings. '''

def make_pizza(size, *toppings):
    print(f"\nmaking {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('medium', 'pepperoni')
make_pizza('large', 'chicken', 'cheese', 'olive')