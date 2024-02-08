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
    
