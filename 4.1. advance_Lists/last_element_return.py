# This syntax is quite useful, because you’ll often want to access the last items in a list without knowing 
# exactly how long the list is

cars = ['audi', 'ferrari', 'toyota', 'honda']
print("\nlast car i owned was:" + cars[-1])


#* removing an item using pop() method and storing and printing the last item popped
popped_item = cars.pop() 
print(f"last item popped from the list: {popped_item}")
print(f"new list : {cars}")


#* adding an item to the last at the last
cars.append('honda')
print(f"after adding an item to the list: {cars}")


#* removing an element by value
cars.remove('honda')
print(f"after removing 'honda' from the list: {cars}")


#* inserting an element at specific index
cars.insert(3,'honda')
print(f"after inserting an element at index 3 : {cars}")

#* popping item from any position in a list

cars.pop(0)
print(f"the first item is popped from the list: {cars}")
