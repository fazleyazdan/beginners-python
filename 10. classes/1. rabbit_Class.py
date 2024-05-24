
class Rabbit():
    
    def __init__(self, name, age) :
        self.name = name
        self.age = age
        
    def bendEar(self):
        print(f"{self.name} rabbit is bending its ears")

    def standing(self):
        print(f"{self.name} is standing on two feet")

#! Instance of the class
my_rabbit = Rabbit('white', 2)


print(f"the name of my rabbit is {my_rabbit.name}")          #! Accessing attributes of the class
print(f"the age of the rabbit is {my_rabbit.age}")

my_rabbit.bendEar()                                          #! Accessing methods of class


#* we can usually assume that a capitalized name like Dog refers to a class, 
#* and a lowercase name like my_dog refers to a single instance created from a class.

''' We define the __init__() method to have three parameters: self, name, and age. 
The self parameter is required in the method definition, and it must come first, before the other parameters. 
It must be included in the definition because when Python calls this method later (to create an instance of Rabbit), 
the method call will automatically pass the self argument.
 
Every method call associated with an instance automatically passes self, 
which is a reference to the instance itself; it gives the individual instance 
access to the attributes and methods in the class. When we make an 
instance of Rabbit, Python will call the __init__() method from the Rabbit class. 
We'll pass Rabbit() a name and an age as arguments; self is passed automatically, so we don't need to pass it. Whenever we want to make an instance 
from the Rabbit class, we'll provide values for only the last two parameters, name
and age.

The two variables defined in the body of the __init__() method each 
have the prefix self. Any variable prefixed with self is available to every 
method in the class, and we'll also be able to access these variables through 
any instance created from the class. The line self.name = name takes the 
value associated with the parameter name and assigns it to the variable name, 
which is then attached to the instance being created. The same process 
happens with self.age = age. Variables that are accessible through instances 
like this are called attributes.

'''


