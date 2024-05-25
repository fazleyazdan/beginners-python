
# Restaurant: Make a class called Restaurant. T
# he __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of information, 
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. 
# Print the two attributes individually, and then call both methods

class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"cuisine type: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")
        
restaurant = Restaurant('Monal', 'sea food')

print(f"\nattribute 1: {restaurant.restaurant_name}")
print(f"attribute 2: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()


print("\n------------ Task 2 ------------\n")

# Three Restaurants: Start with your class from the above Exercise. 
# Create three different instances from the class, and call describe_restaurant() for each instance.

restaurant_1 = Restaurant('Bait ul Arab', 'mandi')
restaurant_2 = Restaurant('Savour Foods', 'savour')
restaurant_3 = Restaurant('Khyber Shinwari', 'beef karahi')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
