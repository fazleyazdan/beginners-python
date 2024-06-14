from car import Car, ElectricCar                     #! importing multiple classes from module
from car import ElectricCar                          #! importing single class from module
from car import *                                    #! importing all classes from module
from car import ElectricCar as EC                    #! using aliases 


ecar_obj = ElectricCar('Honda', 'wiesel', 2024)
ecar_obj.battery_size = 30

print(ecar_obj.descriptive_name())
ecar_obj.describe_battery()
ecar_obj.read_odometer()

