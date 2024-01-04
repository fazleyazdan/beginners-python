# You are creating two lists, my_foods and friend_foods, and making a copy of the elements from my_foods into friend_foods.
# The [:] syntax copies all elements from the beginning to the end of the list.

my_foods = ['talbina' , 'honey' , 'red beans']

friend_foods = my_foods[:]

friend_foods.append('yogurt')

print(" my foods are:", my_foods)

print(f"\n my friends favorite foods are: {friend_foods}")

