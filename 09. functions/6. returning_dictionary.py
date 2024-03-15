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
