class car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
        #* default value attribute
        self.odometer_reading = 0
        
    
    def descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
        
    def update_odometer(self, mileage):                #! method for updating dynamic attribute
        self.odometer_reading = mileage
        return mileage

my_car = car('audi', 'a4', 2024)
print(my_car.descriptive_name())
    

#! Setting a Default Value for an Attribute   
#* for default value, we don't need to pass its value when creating instance. as it has a default value 
#* in the above 'car class' an attribute 'odometer_reading' has a value of 0

my_car.read_odometer() 


#! Modifying Attribute ValuesYou can change an attribute’s value in three ways: 
#* you can change the value directly through an instance, 
#* set the value through a method, 
#* or increment the value (add a certain amount to it) through a method. Let’s look at each of these approaches.

#! Modifying an Attribute’s Value Directly

print('\n--------- modifying attributes value directly --------')
my_car.odometer_reading = 77
my_car.read_odometer()


#! Modifying an Attribute’s Value Through a Method

''' It can be helpful to have methods that update certain attributes for you. 
Instead of accessing the attribute directly, you pass the new value to a 
method that handles the updating internally '''

print('\n--------- modifying attributes value through method --------')
print(f"This car has {my_car.update_odometer(777)} miles on it")


