# Number Served: Start with your program from Task 1 of assignment-1. 
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, and then change this value and print it again.

# Add a method called set_number_served() that lets you set the number of 
# customers that have been served. Call this method with a new number and print the value again.

# Add a method called increment_number_served() that lets you increment 
# the number of customers who’ve been served. Call this method with any number 
# you like that could represent how many customers were served in, say, a day of business

class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
              
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"cuisine type: {self.cuisine_type}")
        
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")
        
        
    def set_number_served(self, noCustomers):
        self.number_served = noCustomers


    def increment_number_served(self, incrementVal):
        if incrementVal < 0:
            print(f"\nnumber of customer should not be in Negative")
        else:
            self.number_served += incrementVal
        
            
restaurant = Restaurant('Dam Pookh', 'Steak')

print(f"\n{restaurant.restaurant_name} has served {restaurant.number_served} customers") 
restaurant.number_served = 7
print(f"\n{restaurant.restaurant_name} has served {restaurant.number_served} customers") 
       
#! num of customer served with a method

restaurant.set_number_served(8)
print(f"\nTotal number of served customers by {restaurant.restaurant_name} : {restaurant.number_served}")

#! Incrementing number of served Customers

restaurant.increment_number_served(-5)
print(f"\nTotal number of served customers after Increment: {restaurant.number_served}")
