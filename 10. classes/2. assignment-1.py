
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
        print(f"name of the restaurant is: {self.restaurant_name}")
        print(f"cuisine type is {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")
        
restaurant = Restaurant('Monal', 'sea food')

print(f"attribute 1: {restaurant.restaurant_name}")
print(f"attribute 2: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()