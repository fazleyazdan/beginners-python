# Person: Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. 
# Print each piece of information stored in your dictionary.

person = {'first name': 'Fazle',
          'last name': 'yazdan',
          'age': '27',
          'city': 'islamabad',
        }

print(person['first name'], end=" ")               #* use end to print the next statement in the same line
print(person['last name'])
print(person['age'])
print(person['city'])


# Use a dictionary to store people’s favorite numbers. 
# Think of five names, and use them as keys in your dictionary. 
# Think of a favorite Dictionaries number for each person, and store each as a value in your dictionary. 
# Print each person’s name and their favorite number. 
# For even more fun, poll a few friends and get some actual data for your program.

fav_num = {'jawad': '7',
           'kamran':'5',
           'asad ali':'7',
           'tariq':'3',
           'imran':'1',
           }

print(f"jawad's fav number is {fav_num['jawad']}")
print(f"Kamran's fav number is {fav_num['kamran']}")
print(f"asad ali's fav number is {fav_num['asad ali']}")
print(f"tariq's fav number is {fav_num['tariq']}")
print(f"imran's fav number is {fav_num['imran']}")

#! by using loop you can reduce time and number of code lines
print()
for key, value in fav_num.items():
  print(f"{key}'s fav number is: {value}") 
  