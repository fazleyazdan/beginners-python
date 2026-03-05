
#! Styling Functions

''' You need to keep a few details in mind when you're styling functions. 
Functions should have descriptive names, and these names should use 
lowercase letters and underscores. Descriptive names help you and others 
understand what your code is trying to do. Module names should use these 
conventions as well.

Every function should have a comment that explains concisely what 
the function does. This comment should appear immediately after the 
function definition and use the docstring format. In a well-documented 
function, other programmers can use the function by reading only the 
description in the docstring. They should be able to trust that the code 
works as described, and as long as they know the name of the function, the 
arguments it needs, and the kind of value it returns, they should be able to 
use it in their programs.

If you specify a default value for a parameter, no spaces should be used 
on either side of the equal sign: 
e.g.
def function_name(parameter_0, parameter_1='default value')

The same convention should be used for keyword arguments in function calls:
e.g.
function_name(value_0, parameter_1='value') 

