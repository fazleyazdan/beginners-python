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
    'hameed': 'ruby',            
     }

s_language = fav_languages['shadman'].title()

print(f"favorite language of shadman is {s_language}")

# For dictionaries specifically, you can use the get() method to set 
# a default value that will be returned if the requested key doesn’t exist.
# if value not found for a key 'none' default value is returned.

no_language = fav_languages.get('ali', "value for 'ali' does not exist")
print(no_language)
no_language = fav_languages.get('ali')                            # returns NONE
print(no_language)