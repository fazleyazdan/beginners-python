# lists in python

cars = ['audi', 'ferrari', 'toyota', 'honda']
print(cars)

print()                          
message = f'my first car was not a {cars[1].title()}'      
print(message)

# appending in list
cars.append('kia')
print(f"\n after appending: ")   #! '\n' statement is for new line spacing
for car in cars:                #! using for loop to iterate and print value of list one by one
    print(car)


# removing specific value from a list 
cars.remove('ferrari')
print(f"\n after removing specific value:")
print(cars)

    
# reversing the list
cars.reverse()
print(f"\n after reversing the list: ")
print(cars)


# printing the length of a list
print(f"\n length of cars ", len(cars))

#  sorting the list by alphabets
cars.sort()
print(f"\n after sorting the list:")
print(cars)
    
# making copy of a list
# print()
cars_copy = cars.copy()                 
print(f"\n after copying the list:")
print(cars_copy)



