''' Sometimes you won't know ahead of time how many arguments a function needs to accept. 
    Fortunately, Python allows a function to collect an arbitrary number of arguments from the calling statement.
    For example, consider a function that builds a pizza. It needs to accept a 
    number of toppings, but you can't know ahead of time how many toppings a 
    person will want. The function in the following example has one parameter, 
    *toppings, but this parameter collects as many arguments as the calling line 
    provides:'''
    
def make_pizza(*toppings):
    print("\npizza toppings:")
    print(toppings)
        
make_pizza('pepperoni')
make_pizza('cheese', 'salad', 'chicken')

#* The asterisk in the parameter name *toppings tells Python to make a tuple called toppings, 
#* containing all the values this function receives.


#! Lets print it one by one by looping through it

print("\n-------------------------------------------")
print("\nPrinting after Modification - for loop")

def make_pizza(*toppings):
    print("\npizza toppings:")
    for topping in toppings:
        print(f'- {topping}')
        
make_pizza('pepperoni')
make_pizza('cheese', 'salad', 'chicken')
