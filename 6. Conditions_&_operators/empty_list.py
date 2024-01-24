# This time we start out with an empty list of collection. 
# Instead of jumping right into a for loop, we do a quick check first. 
# When the name of a list is used in an if statement, Python returns True if the list contains at least one item; 
# an empty list evaluates to False.

checking_list = []

if checking_list:
    for x in checking_list:
        print(f"adding to your collection: {x}")
        print("finished making your collection")
else:
        print("are you sure you don't want to add anything to your collection")   