# Make a list of five or more usernames, including the name 'admin'. 
# Imagine you are writing code that will print a greeting to each user after they log in to a website. 
# Loop through the list, and print a greeting to each user.
# • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again

usernames = ['ali', 'kamran', 'shadman', 'admin', 'abdullah']

for user in usernames:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"welcome {user}!")

        
# No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct message is printed.

while usernames:
    usernames.pop()
    
if usernames:
    print("hello all")
else:
    print("sorry there are no users left")

print(usernames)


# Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. 
# Make sure one or two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already been used. 
# If it has, print a message that the person will need to enter a new username. 
# If a username has not been used, print a message saying that the username is available.

current_users = ['ANEES', 'kamran', 'shadman', 'admin', 'abdullah']

new_users = ['shahid' , 'ANees', 'ABDULLAH', 'usama', 'ahtisham']

for user in new_users:
    if user in current_users:
        print(f"the username ({user}) already exist please enter a new username")
    else:
        print(f"this username ({user}) is available")


# • Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
# (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

print()
lower_current_user = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in lower_current_user:
         print(f"the username ({new_user}) already exist please enter a new username")
    else:
         print(f"this username ({new_user}) is available")

