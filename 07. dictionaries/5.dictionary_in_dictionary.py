# You can nest a dictionary inside another dictionary, 
#* but your code can get complicated quickly when you do. 
# For example, if you have several users for a website, each with a unique username, 
#* you can use the usernames as the keys in a dictionary. 
# You can then store information about each user by using a dictionary 
#* as the value associated with their username.

users = {'fy':
         {'first name': 'fazle',
          'last name': 'yazdan',
          'location': 'islamabad'},
          'jk': 
          {'first name': 'jawad',
           'last name': 'khan',
           'location': 'kpk'}
          }

for user_key, user_val in users.items():
    print(f"\nUsername: {user_key.title()}")
    fullname = f"{user_val['first name']} {user_val['last name']}"
    location = user_val['location']
    
    print(f"\tFull name: {fullname}")
    print(f"\tLocation: {location}")
    