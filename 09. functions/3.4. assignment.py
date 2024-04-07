# Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sandwich that’s being ordered. 
# Call the function three times, using a different number of arguments each time.

print("\n------------ Task 1 ------------\n")

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

print("\n------------ Task 2 ------------\n")

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

userInfo = build_profile('fazle', 'yazdan', location = 'Islamabad', field = 'SQA', favorite_food = 'dates')
print(f"{userInfo}\n")


print("\n------------ Task 3 ------------\n")

# Cars: Write a function that stores information about a car in a dictionary. 
# The function should always receive a manufacturer and a model name. 
# It should then accept an arbitrary number of keyword arguments. 
# Call the function with the required information and two other name-value pairs, 
# such as a color or an optional feature. Your function should work for a call like this one:

# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was stored correctly

def car_info(manufacturer, model_name, **info):
    print("info about the car:")
    info['manufacturer'] = manufacturer
    info['model'] = model_name
    return info
    
store_info = car_info('Tesla', '2023', color = 'white', tow_package = 'True')
print(store_info)
