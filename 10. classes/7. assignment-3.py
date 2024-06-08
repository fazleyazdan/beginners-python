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


print("\n------------ Task 2 ------------\n")

# Admin: An administrator is a special kind of user. 
# Write a class called Admin that inherits from the User class you wrote in assignment_2-2 
# Add an attribute, privileges, that stores a list of strings like "can add post", 
# "can delete post", "can ban user", and so on. 
# Write a method called show_privileges() that lists the administrator’s set of privileges. 
# Create an instance of Admin, and call your method.

class User():
    
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        
    def describe_user(self, age, profession):
        print(f"\tUser name: {self.first_name + ' ' + self.last_name}")
        print(f"\tUser age: {age}")
        print(f"\tUser profession: {profession}")
        
    def greet_user(self):
        print(f"\nHello {self.first_name + ' ' + self.last_name}! Welcome to beginners Python")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    
    def __init__(self, privileges):
        # self.privileges = privileges                                      #! uncomment this & the instances 
        self.privileges_obj = Privileges(privileges)                        #! Privileges class Obj
    
        
    def show_privileges(self):
        print(f"Following are Admins privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")
            
# admin = Admin(['can add post', 'can add user'])
# admin.show_privileges()


print("\n------------ Task 3 ------------\n")

# Privileges: Write a separate Privileges class. 
# The class should have one attribute, privileges, that stores a list of strings like
# like "can add post", "can delete post", "can ban user", and so on. 
# Move the show_privileges() method to this class. 
# Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges

class Privileges:
    
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Following are Admins privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")
            
    
admin_obj = Admin(['can add user', 'can delete user'])
admin_obj.privileges_obj.show_privileges()
