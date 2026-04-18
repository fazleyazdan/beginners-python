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
    
    
    #* Incrementing an Attribute’s Value Through a Method
    def increment_odometer(self,mileage):
        if mileage < 0:
            return print("\nyou can't enter negative values")
        else:
            self.odometer_reading += mileage


class Battery:
    
    def __init__(self, battery_size = 40):                    #! default value for battery_size in case no value is provided
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"\nThis Car has {self.battery_size}-KWh battery")
        
    def get_range(self):
        
        if self.battery_size >= 40 and self.battery_size < 50:
            range = 70
        elif self.battery_size >= 50 and self.battery_size < 70:
            range = 225 
        elif self.battery_size >= 70 and self.battery_size < 100:
            range = 300
        elif self.battery_size == 100:
            range = 700
        print(f"\tThis car can go about {range} miles on {self.battery_size} percent battery")
        
    def upgrade_battery(self, new):
        if self.battery_size == None:
            self.battery_size = 65
        else:
            self.battery_size = new        
    
