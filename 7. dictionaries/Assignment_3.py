# Start with the program you wrote in assignment 1. 
# Make two new dictionaries representing different people, 
# and store all three dictionaries in a list called people. 
# Loop through your list of people. As you loop through the list, 
# print everything you know about each person.

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
print("=================================")
for i,person in enumerate(persons_list,start=1):
    print(f"\nperson {i} info are as follows:")
    for key, val in person.items():
        print(f"\n{key}:{val}")

#! Make several dictionaries, where each dictionary represents a different pet. 
#* In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. 
#* Next, loop through your list and as you do, 
# print everything you know about each pet
        
