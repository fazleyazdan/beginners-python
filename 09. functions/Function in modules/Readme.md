<!--  One advantage of functions is the way they separate blocks of code from your main program. 
When you use descriptive names for your functions, your programs become much easier to follow. 
You can go a step further by storing your functions in a separate file called a module and then importing
that module into your main program.
An import statement tells Python to make the code in a module available in the currently running program file.
Storing your functions in a separate file allows you to hide the details of 
your program’s code and focus on its higher-level logic. 
It also allows you to reuse functions in many different programs. 
When you store your functions in separate files, you can share those files with other programmers without 
having to share your entire program. 
Knowing how to import functions also allows you to use libraries of functions that other programmers have written. 
There are several ways to import a module,  -->


#### e.g. There is a module named *pizza.py* & it has a function name *make_pizza*

#### now i want to import the module into another file called *making_pizza.py*.

```python

# Importing an entire Module

import pizza

# each function in the module is available through the following syntax:

module_name.function_name()

# Importing Specific Functions

from module_name import function_name

# You can import as many functions as you want from a module by separating each function’s name with a comma:

from module_name import function_0, function_1, function_2

# The making_pizzas.py example would look like this if we want to import just the function we’re going to use:

from pizza import make_pizza

# Using as to Give a Function an Alias

from pizza import make_pizza as mp

# Using as to Give a Module an Alias

import pizza as p

# Importing All Functions in a Module

from pizza import *

'''The asterisk in the import statement tells Python to copy every function 
from the module pizza into this program file. Because every function is 
imported, you can call each function by name without using the dot notation
However, it’s best not to use this approach when you’re working with larger 
modules that you didn’t write: if the module has a function name that matches 
an existing name in your project, you can get unexpected results. '''

'''The best approach is to import the function or functions you want, or 
import the entire module and use the dot notation. This leads to clear code 
that’s easy to read and understand '''




```