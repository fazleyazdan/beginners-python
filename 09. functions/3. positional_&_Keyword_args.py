# Order Matters in Positional Arguments
# you have to pass arguments which matches the order of parameters.

print("\n*** Positional Arguments: ***")
def describe_pet(pet_type, pet_name):
    print(f"\ni have {pet_type}")
    print(f"\tmy {pet_type} name is {pet_name.title()}")
    
describe_pet('cat', 'tom')
describe_pet('Rabbit', 'hargosh')   

#! You can get unexpected results if you mix up the order of the arguments in 
#! a function call when using positional arguments: see the example below

describe_pet('snatcher', 'Parrot') 

#* ============================================================================ #

#* A keyword argument is a name-value pair that you pass to a function. 
# You directly associate the name and the value within the argument, so when you 
# pass the argument to the function, there’s no confusion

print("\n*** Keyword Arguments: ***")
#* A keyword argument is a name-value pair that you pass to a function. 
# You directly associate the name and the value within the argument, 
# so when you pass the argument to the function, there’s no confusion.
#!  When you use keyword arguments, be sure to use the exact names of the parameters in the function’s definition

def describe_pet(pet_type = 'kangaroo', pet_name = 'jumper'):
    print(f"\ni have {pet_type} and his name is {pet_name}")

describe_pet()