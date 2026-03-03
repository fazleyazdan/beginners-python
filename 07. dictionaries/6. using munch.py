# munch is a Python library that provides a dictionary subclass which allows keys to be accessed as attributes. 
# This means that, in addition to using the standard dictionary syntax to access values, you can use dot notation, 
# which can make the code cleaner and more readable.
#* to use munch first install the library using 'pip install munch' & then import it

#! here is an example to demonstrate the usage of munch:

from munch import Munch

# Creating a Munch object
data = Munch()

# Adding key-value pairs
data.name = "Khalid bin Waleed"
data.age = 30

# Accessing values using dot notation
print(data.name)  # Output: Khalid bin Waleed
print(data.age)   # Output: 30

# You can still access values using dictionary syntax
print(data['name'])  # Output: Khalid bin Waleed
print(data['age'])   # Output: 30

