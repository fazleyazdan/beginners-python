
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


print("\n------------ Task 3 ------------\n")

# Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

class User():
    
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_user(self, age, profession):
        print(f"\tUser name: {self.first_name + ' ' + self.last_name}")
        print(f"\tUser age: {age}")
        print(f"\tUser profession: {profession}")
        
    def greet_user(self):
        print(f"\nHello {self.first_name + ' ' + self.last_name}! Welcome to beginners Python")
        
        
person = User('ali', 'khan')
person.describe_user(20, 'Rescuer')

person_1 = User('fazle', 'yazdan')
person_1.greet_user()
person_1.describe_user(25, 'Software Tester')

person_2 = User('jawad', 'khan')
person_2.greet_user()
person_2.describe_user(24, 'Quality Assurance')


