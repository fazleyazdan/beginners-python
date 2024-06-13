class Car:
    
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
        
