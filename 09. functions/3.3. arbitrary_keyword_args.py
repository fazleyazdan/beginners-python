'''Sometimes you'll want to accept an arbitrary number of arguments, but you 
   won't know ahead of time what kind of information will be passed to the function.
        
    In this case, you can write functions that accept as many key-value     
    pairs as the calling statement provides. One example involves building user profiles: 
    you know you'll get information about a user, but you're not sure what kind of information you'll receive.'''
    
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

userInfo = build_profile('fazle', 'yazdan', location = 'Islamabad', field = 'SQA')
print(userInfo)


''' The double asterisks before the parameter **user_info cause Python to create 
a dictionary called user_info containing all the extra name-value pairs the 
function receives. Within the function, you can access the key-value pairs in 
user_info just as you would for any dictionary.'''