from car import Car

#! in the above statement we have imported car class to use its functionalities 

car_obj = Car('audi', 'a4', 2024)
print(car_obj.descriptive_name())

car_obj.odometer_reading = 77
car_obj.read_odometer()