# Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the change.
# • The restaurant changes its menu, replacing two of the items with different foods. 
# Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.


foods_tuple = ('grilled beef', 'grilled chicken', 'biryani', 'kabali pulao', 'talbina')

for food in foods_tuple:
    print(food)
    
# foods_tuple [1] = 'kebab'                            # will throw an error

print("\nre writing tuples with some new foods")

foods_tuple = ('grilled beef', 'chickpeas', 'red beans', 'kabali pulao', 'talbina')

for food in foods_tuple:
    print(food)