# lists in python

cars = ['audi', 'ferrari', 'toyota', 'honda']

message = f'my first car was not a {cars[1].title()}'      
print(message)
print()

# appending in list
cars.append('kia')

print("after appending: ")
for car in cars:
    print(car)


# removing specific value from a list 
cars.remove('ferrari')

print()
print("after removing specific value:")
for car in cars:
    print(car)
    
# reversing the list
print()
print("after reversing the list")
cars.reverse()
for car in cars:
    print(car)

# printing the length of a list
print()
print("length of cars ", len(cars))

#  sorting the list by alphabets
print()

cars.sort()
for car in cars:
    print(car)
    
# making copy of a list
print()
print("after copying the list")

cars_copy = cars.copy()
for carcopy in cars_copy:
    print(carcopy)
