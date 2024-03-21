# Passing a list to a function
#* we will pass a list of user and then call the function to greet each user


def greet_users(listusers):
    for user in listusers:
        print(f"\nHello {user}!")

usernames = ['ali', 'kamran', 'shadman']
greet_users(usernames)

#! ==================== modifying list in function ==================== #
