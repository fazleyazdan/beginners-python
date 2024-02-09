# Task 1:
# Rivers: Make a dictionary containing three major rivers and the country each river runs through. 
# One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary

rivers = {'amazon': 'brazil', 'nile': 'egypt', 'chang jian': 'china'}

for key,val in rivers.items():
    print(f"\n{key} runs through {val}")

print("\nrivers included in dictionary")
for key in rivers.keys():
    print(key)
    
print("\ncountries included in dictionary")
for val in rivers.values():
    print(val)
    

#! Task 2:
# . Polling: Use the code in favorite_languages.py
# • Make a list of people who should take the favorite languages poll. Include 
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have 
# already taken the poll, print a message thanking them for responding. 
# If they have not yet taken the poll, print a message inviting them to take 
# the poll

fav_languages =  {
    'kamran': 'c',
    'shadman': 'python', 
    'jawad': 'javascript',
     }

print("")
poll_lists = ['shadman', 'jawad', 'hameed', 'ali', 'kamran']

for plist in poll_lists:
    if plist in fav_languages.keys():
        print(f"\n{plist} Thank you! for participating in polls")
    else:
        print(f"\n{plist} please participate in poll, you are invited..")
        