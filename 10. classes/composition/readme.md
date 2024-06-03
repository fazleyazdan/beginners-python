#### Instances as Attributes

* When modeling something from the real world in code, you may find that 
 you’re adding more and more detail to a class. You’ll find that you have a 
 growing list of attributes and methods and that your files are becoming 
 lengthy. In these situations, you might recognize that part of one class can 
 be written as a separate class. You can break your large class into smaller 
 classes that work together; this approach is called composition.
 For example, if we continue adding detail to the ElectricCar class, we 
 might notice that we’re adding many attributes and methods specific to 
 the car’s battery. When we see this happening, we can stop and move those 
 attributes and methods to a separate class called Battery. Then we can use a 
 Battery instance as an attribute in the ElectricCar class: