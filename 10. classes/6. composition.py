""" When modeling something from the real world in code, you may find that 
 you're adding more and more detail to a class. You'll find that you have a 
 growing list of attributes and methods and that your files are becoming 
 lengthy. In these situations, you might recognize that part of one class can 
 be written as a separate class. You can break your large class into smaller 
 classes that work together; this approach is called composition.
 For example, if we continue adding detail to the ElectricCar class, we 
 might notice that we're adding many attributes and methods specific to 
 the car's battery. When we see this happening, we can stop and move those 
 attributes and methods to a separate class called Battery. Then we can use a 
 Battery instance as an attribute in the ElectricCar class: 
 
For example, if we continue adding detail to the ElectricCar class, we 
might notice that we're adding many attributes and methods specific to 
the car's battery. When we see this happening, we can stop and move those 
attributes and methods to a separate class called Battery. Then we can use a 
Battery instance as an attribute in the ElectricCar class: """
 

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
    
    
