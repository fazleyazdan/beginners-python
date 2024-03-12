# A function doesn’t always have to display its output directly. 
# Instead, it can process some data and then return a value or set of values. 
#* The value the function returns is called a return value.

def get_formatted_name(first, last):
    """Return Neatly formated full name"""
    full_name = f"{first} {last}"
    return full_name.title()

#* When you call a function that returns a value, you need to provide a variable that the return value can be assigned to.
my_name= get_formatted_name('fazle', 'yazdan')
print(f"\n{my_name}")

#! ================================================ # 

#! Making an Argument Optional
#* we want to expand get_formatted_name() to handle middle names as well. 
# But middle names aren’t always needed, 
# To make get_formatted_name() work without a middle name, 
# we set the default value of middle_name to an empty string and move it to the end of the list of parameters

def get_middle_name(first, last, middle = ''):
    """Return Neatly formated full name"""               
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
        
    return full_name.title()

#* When you call a function that returns a value, you need to provide a variable that the return value can be assigned to.
my_name= get_middle_name('fazle', 'yazdan')
print(f"\n{my_name}")
my_name= get_middle_name('khabib', 'nur', 'the eagle')
print(f"\n{my_name}")
