''' You don’t always have to start from scratch when writing a class. If the class 
you’re writing is a specialized version of another class you wrote, you can 
use inheritance. When one class inherits from another, it takes on the attributes and methods of the first class. The original class is called the parent 
class, and the new class is the child class. The child class can inherit any 
or all of the attributes and methods of its parent class, but it’s also free to 
define new attributes and methods of its own. '''

#! he __init__() Method for a Child Class
# When you’re writing a new class based on an existing class, 
# you’ll often want to call the __init__() method from the parent class. 
# This will initialize any attributes that were defined in the parent __init__() method and make 
# them available in the child class.

#* Lets inherit an electric car from the 'car Class'.

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

class ElectricCar(car):
    
    def __init__(self, make, model, year):
        
        ''' Calling init from the parent class, which initializes attributes'''
        super().__init__(make, model, year)
        

my_ecar = ElectricCar('nissan', 'leaf', 2024)

print(my_ecar.descriptive_name())

""" When you create a child class, the parent class must be part of the current file 
and must appear before the child class in the file. We then define the child class, ElectricCar . 
The name of the parent class must be included in parentheses in the definition of a child class. 
The __init__() method takes in the information required to make a Car
instance """

""" The super() function is a special function that allows you to call a 
method from the parent class. This line tells Python to call the __init__()
method from Car, which gives an ElectricCar instance all the attributes 
defined in that method. The name super comes from a convention of calling 
the parent class a superclass and the child class a subclass. """

