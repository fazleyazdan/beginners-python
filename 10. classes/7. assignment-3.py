# Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in assignment_2-1. 
# Add an attribute called flavors that stores a list of ice cream flavors. 
# Write a method that displays these flavors. 
# Create an instance of IceCreamStand, and call this method.

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
            

class iceCreamStand(Restaurant):
    
    def __init__(self, flavors):
        self.flavors = flavors
        
    
    def display_flavors(self):
        print("Here are the list of flavors")
        for flavor in self.flavors:
            print(f"\t{flavor}")
        
ice_cream = iceCreamStand(flavors= ['chocolate', 'banana', 'pistachio'])
            
ice_cream.display_flavors()    