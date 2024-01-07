# 1. make a list 
# 2. use if condition having not keyword

banned_users = ['usa', 'israel', 'uk']

user = 'yemen'

if user not in banned_users:
    print(f"{user.title()} : you can post anything you want")
