# Start with the program you wrote in assignment 1. 
# Make two new dictionaries representing different people, 
# and store all three dictionaries in a list called people. 
# Loop through your list of people. As you loop through the list, 
# print everything you know about each person.

print("===== persons task =======")
person_1 = {'first name': 'ali',
          'last name': 'khan',
          'age': '25',
          'city': 'islamabad',
        }

person_2 = {'first name': 'arsalan',
          'last name': 'ahmad',
          'age': '26',
          'city': 'sialkot',
        }

person_3 = {'first name': 'uzair',
          'last name': 'khan',
          'age': '30',
          'city': 'punjab',
        }

persons_list = [person_1,person_2,person_3]

for person in persons_list:
    print(f"\npersons info are as follows:")
    for key, val in person.items():
        print(f"\n{key}:{val}")

#! now lets make  it more dynamic. 
#* instead of this: "persons info are as follows:" 
#* we will write this: "person 1 info are as follows":
print("\n====== dynamic person number =======")
for i,person in enumerate(persons_list,start=1):
    print(f"\nperson {i} info are as follows:")
    for key, val in person.items():
        print(f"\n{key}:{val}")

#* enumerate() is a built-in Python function that allows you to loop over an iterable (like a list) 
# and get both the index of each item and the item itself.
#* persons_list is the iterable being looped over, 
# in this case, a list containing dictionaries representing individual persons.
#* start=1 is an optional parameter for enumerate() that specifies the starting index value. By default, enumerate() starts the index from 0, but here we're setting it to start from 1.
#* i is the index of the current item being processed in the loop.
#* person is the actual item itself, in this case, 
#* a dictionary representing the details of each person.So, in each iteration of the loop:
#* i will hold the index of the current person in the list, starting from 1 due to start=1.
#* person will hold the dictionary representing the details of the current person.
#* This allows you to access both the index and the item in the list at the same time within the loop.

#* ============================================== #

#! Make several dictionaries, where each dictionary represents a different pet. 
#* In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. 
#* Next, loop through your list and as you do, 
# print everything you know about each pet

print("\n====== pets task task =======")
pet1 = {  'pet': 'rabbit',
          'owner name': 'ali',
          'color': 'white & brown',
        }

pet2 = {  'pet': 'cat',
          'owner name': 'muhammad haneef',
          'color': 'white',
        }

pet3 = {  'pet': 'parrot',
          'owner name': 'shadman',
          'color': 'green',
        }

pets = [pet1, pet2, pet3]

for i, pet in enumerate(pets, start=1):
    print(f"\npet{i} info:")
    for key,val in pet.items():
        print(f"\t{key}:{val}")

#* ============================================== #

#* Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, 
# and store one to three favorite places for each person.  
# Loop through the dictionary, and print each person’s name and their favorite places
print("\n===== Favorite place task =======")
favorite_places = {'fazleyazdan': ['shogran', 'skardu', 'islamabad'],
                   'ali khan': ['spin ghar', 'swat', 'peshawar'],
                   'hameed khan': ['dir', 'islamabad', 'sawabi']}

for key, val in favorite_places.items():
    print(f"\n{key.title()}'s favorite places are:")
    for v in val:
        print(f"\t{v.title()}")

#! Favorite Numbers: 
# Modify your program from Assignment so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.
print("\n===== Favorite numbers task =======")

fav_num = {'jawad': ['7', '5', '3'],
           'kamran':['1', '9'],
           'asad ali':['3', '7', '11'],
           }

for key, val in fav_num.items():
        print(f"\n{key.title()}'s favorite numbers:")
        for v in val:
                print(f"\t{v}")