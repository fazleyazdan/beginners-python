# A function doesn’t always have to display its output directly. 
# Instead, it can process some data and then return a value or set of values. 
#* The value the function returns is called a return value.

def return_fname(first, last):
    """Return Neatly formated full name"""
    full_name = f"{first} {last}"
    return full_name.title()

my_name= return_fname('fazle', 'yazdan')
#* When you call a function that returns a value, you need to provide a variable that the return value can be assigned to.
print(my_name)

