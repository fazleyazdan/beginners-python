# The if-elif-else chain is powerful, but it’s only appropriate to use when you just need one test to pass.
# As soon as Python finds one test that passes, it skips the rest of the tests. 
# This behavior is beneficial, because it’s efficient and allows you to test for one specific condition

age = 27

if age >=22:
    print("you are now mature enough to differentiate between right and wrong")
elif age ==27:
    print("you have to control your desires in order to get closer to your creator")
else:
    print("devil is always there. he does not sleep, make your defenses strong")
    
    
# python does not require else in the last

age_1 =26

if age < 25:
    price = 20
elif age > 30:
    price = 25
elif age >= 26:
    price = 15
elif age == 30:
    price = 20

print(f"\nthe price for your admission fee is: {price} RS")


# However, sometimes it’s important to check all conditions of interest. 
# In this case, you should use a series of simple if statements with no elif or else blocks. 
# This technique makes sense when more than one condition could be True, and you want to act on every condition that is True.

cars = ['audi', 'bmw', 'ferrari', 'honda']

my_fav = 'honda'
not_my_fav = 'bmw'
if my_fav in cars:
    print(f"my fav car is: {my_fav}")
    
if not_my_fav in cars:
    print("i don't like: ", not_my_fav)