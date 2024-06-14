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