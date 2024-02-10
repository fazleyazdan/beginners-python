# Sometimes you’ll want to store multiple dictionaries in a list, or a list of items as a value in a dictionary. 
# This is called nesting. You can nest dictionaries inside a list, a list of items inside a dictionary, 
# or even a dictionary inside another dictionary. 
# Nesting is a powerful feature, as the following examples will demonstrate.

car_0 = {'model': '2015', 'brand': 'Audi', 'condition': 'Good'}
car_1 = {'model': '2016', 'brand': 'Bmw', 'condition': 'Good'}
car_2 = {'model': '2017', 'brand': 'Ferrari', 'condition': 'Excellent'}

# storing dictionaries in a list
cars_list = [car_0, car_1, car_2]

print("\nprinting dictionaries list\n")
print(f"{cars_list}\n")

# if you want to print dictionaries in list one by one use for loop
print("printing dictionaries in a list one by one\n")
for car in cars_list:
    print(car)
    

# A more realistic example would involve more than three cars with 
# code that automatically generates each car. 
# In the following example, we use range() to create a fleet of 10 cars

# make an empty list to store dictionaries
cars_list_2 = []     
print("\ngenerates cars using range function\n")

#! These aliens all have the same characteristics, but Python considers each 
#! one a separate object, which allows us to modify each alien individually
for car in range(10):
    new_car = {'model': '2015', 'brand': 'Audi', 'condition': 'Good'}
    cars_list_2.append(new_car) 
print(cars_list_2)


print("\nShow first 5 cars\n")
for car in cars_list_2[:5]:
    print(car)
    
#* Modify first 3 cars
for car in cars_list_2[:3]:
    if car['model'] == '2015':
        car['model'] = '2024'
        car['brand'] = 'Toyota'
        car['condition'] = 'Excellent'
        
print("\nAfter modifying first 3 cars\n")
for car in cars_list_2[:5]:
    print(car)

#* i have given condition 'model', because there may be other items. 
#* so it's a good idea to modify specific items. for example


#* through range(), you can generate same items. but if you want to modify you can do so
#* by following below techniques

#! modify cars from 4 to 6
for car in cars_list_2[:6]:
    if car['model'] == '2015':
        car['model'] = '2017'
        car['brand'] = 'ferrari'
        car['condition'] = 'Average'
    elif car['model'] == '2024':
        car['condition'] = 'Brand new'
        
print("\nafter playing with the list items.\n")
for car in cars_list_2[:6]:
    print(car)
 