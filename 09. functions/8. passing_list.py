# Passing a list to a function
#* we will pass a list of user and then call the function to greet each user


def greet_users(listusers):
    for user in listusers:
        print(f"\nHello {user}!")

usernames = ['ali', 'kamran', 'shadman']
greet_users(usernames)


#! ==================== modifying list in function ==================== #
#* When you pass a list to a function, the function can modify the list. 
#* Any changes made to the list inside the function’s body are permanent.

#! ==================== Modify list without using function ==================== #
''' Consider a company that creates 3D printed models of designs that users submit. 
    Designs that need to be printed are stored in a list, and after being printed they're moved to a separate list. 
    The following code does this without using functions:'''

print(f"\n**** modifying list without using function ****")
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    

#! ==================== Modify list by using function ==================== #
#* we will reorganize code by making 2 functions of the code. the code will not be changed

print(f"\n**** modifying list by using function ****")
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"\nprinting model: {current_design}")
        completed_models.append(current_design)
    
def show_completed_models(completed_models):
    print(f"\nThe following designs are completed")
    for model in completed_models:
        print(f"\t{model}")
        
unprinted_designs = ['phone case', 'palestine map', 'olive tree']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

'''If we need to print more designs later on, we can simply call Functions print_models() again.
This example also demonstrates the idea that every function should have one specific job. 
The first function prints each design, and the second displays the completed models. 
This is more beneficial than using one function to do both jobs. '''

#! ==================== prevent function from modifying list ==================== #
#* in the above code the 'unprinted_design' becomes empty after popping all of its items
#* sometimes you will need to keep the original list intact and pass a copy of it to function

print(f"\n***** Passing copy of list to function *****")

unprinted_designs = ['phone case', 'palestine map', 'olive tree']
completed_models = []
print_models(unprinted_designs[:],completed_models)              #! unprinted_designs[:] makes copy of the list
show_completed_models(completed_models)
print(f"\nThis is the original list: {unprinted_designs}")