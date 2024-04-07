# Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sandwich that’s being ordered. 
# Call the function three times, using a different number of arguments each time.

print("\n------------ Task 1 ------------")

def make_sandwich(*items):
    print(f"\nMaking sandwich with the Following items:")
    for item in items:
        print(f"\t-{item}")

make_sandwich('chicken')
make_sandwich('beef', 'salad')
make_sandwich('egg', 'salad', 'beef')


# User Profile: Start with a copy of user_profile from 3.3 
# Build a profile of yourself by calling build_profile(), 
# using your first and last names and three other key-value pairs that describe you 

print("\n------------ Task 2 ------------")

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

userInfo = build_profile('fazle', 'yazdan', location = 'Islamabad', field = 'SQA', favorite_food = 'dates')
print(f"\n{userInfo}\n")