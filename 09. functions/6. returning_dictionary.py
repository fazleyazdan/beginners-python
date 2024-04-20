# Returning Dictionary 

def p_dict(first,last):
    '''Return dictionary'''
    person = {'first name': first, 'last name': last}
    return person

store_dict = p_dict('fazle', 'yazdan')
print(f"\n{store_dict}")

#! ================================================== #

#* you can modify it according to your needs. i.e. you can add person age as well
def p_dict(first,last, age = None):
    ''' None, which is used when a variable 
    has no specific value assigned to it. You can think of None as a placeholder 
    value. In conditional tests, None evaluates to False.'''
    
    person = {'first name': first, 'last name': last}
    if age:
        person['age'] = age
    return person

store_dict = p_dict('fazle', 'yazdan', '25')
print(f"\n{store_dict}")

#! ============= Using a Function with a while Loop ================ #

def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

#* When you call a function that returns a value, you need to provide a variable that the return value can be assigned to.
while True:
    print("\nEnter 'q' anytime to quit")
    
    first_n = input("\nplease enter first name: ")
    if first_n == 'q':
        break
    
    last_n =  input("\nplease enter last name: ")
    if last_n == 'q':
        break
    
    store_n = get_formatted_name(first_n, last_n)
    print(f"\nHello {store_n}!")
        
