# we used remove() to remove a specific value from a list. 
#* The remove() function worked because the value we were interested in appeared only once in the list. 
#* But what if you want to remove all instances of a value from a list?

#* Say you have a list of pets with the value 'cat' repeated several times. 
#* To remove all instances of that value, you can run a while loop until 'cat' is no longer in the list,
#* While loop comes handy in this situation

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(f"\n{pets}")

for pet in pets:
    while pet == 'cat':
        
