
#* is there a data type in python which is passed by reference

# In Python, the concept of "pass by reference" or "pass by value" doesn't apply in the same way it does in some other languages. 
# However, Python uses a mechanism called "pass by object reference" or "pass by assignment."

#* Here's how it works:

#* Immutable Objects (e.g., int, float, str, tuple):

# When you pass an immutable object to a function, you're passing a reference to the object, but since the object is immutable, 
# any modifications within the function create a new object. 
# This behavior is similar to "pass by value" in other languages because the original object remains unchanged.

#* Mutable Objects (e.g., list, dict, set):

# When you pass a mutable object to a function, you're passing a reference to the object. 
# Since the object is mutable, any changes made to the object within the function will affect the original object outside the function. 
# This behavior is similar to "pass by reference" in other languages because the original object can be modified.

#* So, mutable objects in Python behave as if they are "passed by reference" because changes to the object within a function affect the original object. 
# Examples of mutable objects include lists, dictionaries, and sets.

#* Here’s a quick example to illustrate:
    
def modify_list(a_list):
    a_list.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

# In this example, my_list is modified by the modify_list function, 
# demonstrating how mutable objects behave similarly to "pass by reference."
