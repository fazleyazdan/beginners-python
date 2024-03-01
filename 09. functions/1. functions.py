# Functions are named blocks of code designed to do one specific job.
# If you need to perform that task multiple times throughout your program, 
# you don’t need to type all the code for the same task again and again; 
# you just call the function dedicated to handling that task, and the call 
# tells Python to run the code inside the function.

def greet_user():
    print("Hello!\n")
greet_user()

"""def greet_user(): This is the function definition, which tells Python the name of the function and, if 
applicable, what kind of information the function needs to do its job. The 
parentheses hold that information."""               

#! above is a comment called 'docstring'. When Python generates documentation 
#* for the functions in your programs, it looks for a string immediately after the function's definition. 
#* These strings are usually enclosed in triple quotes, which lets you write multiple lines.

#! Passing Information to a Function:

def greet_user(username):
    print(f"hello {username}!")
    
greet_user('ali')
greet_user('fazle')
greet_user('hameed')

""" the 'username' in function definition is called 'parameter' i.e. def greet_user(username)
and the values passed to a function in function call are called arguments i.e. greet_user('ali')"""

