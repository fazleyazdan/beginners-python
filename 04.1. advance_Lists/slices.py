# Slices: Using one of the programs you wrote in this chapter, add several 
# lines to the end of the program that do the following:


slices = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']


# • Print the message The first three items in the list are: 
# Then use a slice to print the first three items from that program’s list.
print("first three items in the list")
print(slices[:3])


# • Print the message Three items from the middle of the list are: 
# Then use a slice to print three items from the middle of the list.
print("middle three items in the list")
print(slices[2:5])


# • Print the message The last three items in the list are:
# Then use a slice to print the last three items in the list
print("last three items in the list")
print(slices[4:])                         # or
print(slices[-3:])                        # 0 , -1 , -2 