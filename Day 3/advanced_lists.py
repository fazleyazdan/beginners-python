# lists in python

cars = ['audi', 'ferrari', 'toyota', 'honda']
print(cars)

print()                         #! empty print() statement is for extra line spacing 
message = f'my first car was not a {cars[1].title()}'      
print(message)
print()

# appending in list
cars.append('kia')

print("after appending: ")
for car in cars:                #! using for loop to iterate and print value of list one by one
    print(car)


# removing specific value from a list 
print()

cars.remove('ferrari')
print("after removing specific value:")
print(cars)

    
# reversing the list
print()

cars.reverse()
print("after reversing the list: ")
print(cars)


# printing the length of a list
print()
print("length of cars ", len(cars))

#  sorting the list by alphabets
print()
cars.sort()
print("after sorting the list:")
print(cars)
    
# making copy of a list
print()
cars_copy = cars.copy()
print("after copying the list:")
print(cars_copy)



