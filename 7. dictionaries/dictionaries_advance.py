# A key-value pair is a set of values associated with each other. 
# When you provide a key, Python returns the value associated with that key. 
# Every key is connected to its value by a colon, and individual key-value pairs are separated by commas.

emp = {'name': 'ali', 'age': '27'}
print(f"\nemp dictionary: {emp}")

# storing value of a key in a variable
emp_age = emp['age']
print(f"employe age is: {emp_age}")

# adding new keyvalue to the dictionary
emp['designation'] = 'driver'
print(f"updated emp dictionary: {emp}")

# modifying values of in a dictionary
emp['age'] = '28'
print(f"updated emp age is: {emp['age']}")
print("designation added to dictionary:",emp)

# deleting key-value pair in dictionary
del (emp['age'])
print(f"dictionary after deleting employe_age: {emp}")

# When you know you’ll need more than one line to define a dictionary, press ENTER after the opening brace. 
# Then indent the next line one level (four spaces) and write the first key-value pair, followed by a comma.

fav_languages =  {
    'kamran': 'c',
    'shadman': 'python', 
    'jawad': 'javascript',
    'hameed': 'python',            
     }

s_language = fav_languages['shadman'].title()

print(f"favorite language of shadman is {s_language}")

# For dictionaries specifically, you can use the get() method to set ...
# a default value that will be returned if the requested key doesn’t exist.
# if value not found for a key 'none' default value is returned.

no_language = fav_languages.get('ali', "value for 'ali' does not exist")
print(no_language)

no_language = fav_languages.get('ali')                            # returns NONE
print(no_language)


print("\nlooping through keys only:")
for name in fav_languages.keys():
  print(name)   
  
# Looping through the keys is actually the default behavior when looping through a dictionary, 
# so this code would have exactly the same output if you wrote this.
print("\ndefault behaviour")
for name in fav_languages:
  print(name)
  
# looping through values of dictionary only
print("\nlooping through values only:")

print("following languages has been mentioned in the dictionary:")   
for value in fav_languages.values():
  print(value)

# after temporary sorting
print("\nfollowing fav languages has been mentioned in the dictionary [sorted version]:")   
for value in sorted(fav_languages.values()):
  print(value)

# this approach pulls all the values from the dictionary without checking for repeats.
# To see each number chosen without repetition, we can use a set. 
# A setis a collection in which each item must be unique:

print("\nuse of set to avoid repeatition:")   
for value in set(fav_languages.values()):
  print(value)
  
# looping key, values in a dictionary 

print("\nprinting dictionary key value:")
for key,value in fav_languages.items():
    print(f"{key}'s favorite language is {value}")


# it’s easy to mistake sets for dictionaries because they’re both wrapped in braces. 
# When you see braces but no key-value pairs, you’re probably looking at a set. 
# Unlike lists and dictionaries, sets do not retain items in any specific order.

print("\n making a set")

fav_languages = {'python', 'c', 'javascript', 'python'}
print(fav_languages)