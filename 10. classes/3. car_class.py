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
        
    
    def update_odometer(self, mileage):                #* method for updating dynamic attribute
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"\nyou can't rollback odometer")
        
        return mileage
    
    
    #* Incrementing an Attribute’s Value Through a Method
    def increment_odometer(self,mileage):
        if mileage < 0:
            return print("\nyou can't enter negative values")
        else:
            self.odometer_reading += mileage
        
    
        
my_car = car('audi', 'a4', 2024)
print(my_car.descriptive_name())
    

#! Setting a Default Value for an Attribute   
#* for default value, we don't need to pass its value when creating instance. as it has a default value 
#* in the above 'car class' an attribute 'odometer_reading' has a value of 0

my_car.read_odometer() 

#! Modifying Attribute Values: You can change an attribute’s value in three ways: 
#* you can change the value directly through an instance, 
#* set the value through a method, 
#* or increment the value (add a certain amount to it) through a method. Let’s look at each of these approaches.

#! 1 : Modifying an Attribute’s Value Directly

print('\n--------- modifying attributes value directly --------')
my_car.odometer_reading = 77
my_car.read_odometer()


#! 2 : Modifying an Attribute’s Value Through a Method

''' It can be helpful to have methods that update certain attributes for you. 
Instead of accessing the attribute directly, you pass the new value to a 
method that handles the updating internally '''

print('\n--------- modifying attributes value through method --------')
my_car.update_odometer(345)
my_car.read_odometer()


#! Incrementing an Attribute’s Value Through a Method

print('\n--------- Incrementing attribute through Method --------')
my_car.increment_odometer(100)
my_car.read_odometer()

my_car.increment_odometer(-100)                #* checking with negative values
my_car.read_odometer()

