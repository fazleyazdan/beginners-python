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

print(f"\njawad's fav number is {fav_num['jawad']}")
print(f"Kamran's fav number is {fav_num['kamran']}")
print(f"asad ali's fav number is {fav_num['asad ali']}")
print(f"tariq's fav number is {fav_num['tariq']}")
print(f"imran's fav number is {fav_num['imran']}")

#! by using loop you can reduce time and number of code lines
print()
for key, value in fav_num.items():
  print(f"{key}'s fav number is: {value}") 
  
# A Python dictionary can be used to model an actual dictionary. 
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. 
# You might print the word followed by a colon and then its meaning, 
# or print the word on one line and then print its meaning indented on a second line. 
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

py_glossary = {'dictionary': 'key value pair',
               'loop': 'iteration',
               'list': 'collection of items',
               'tuple': 'immutable',
               'variable': 'a container',
               }

print("Glossary")
for key, value in py_glossary.items():
  print(f"\n{key}")
  print("   ", value)                 #* for indentation
  

print("\nlooping through keys only:")
for name in fav_num.keys():
  print(name)   
# Looping through the keys is actually the default behavior when looping through a dictionary, 
# so this code would have exactly the same output if you wrote this.

print("\ndefault behaviour")
for name in fav_num:
  print(name)
  
# looping through values of dictionary only
print("\nlooping through values only:")

print("following fav number has been mentioned in the dictionary:")   
for value in fav_num.values():
  print(value)

