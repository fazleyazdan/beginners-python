<!--

Object-oriented programming (OOP) is one of the most effective approaches to writing software.
In object-oriented programming, you write classes that represent real-world things and situations,
and you create objects based on these classes. When you write a class, you define the general behavior that a whole category of objects can have.

When you create individual objects from the class, each object is automatically equipped with the general behavior; you can then give each object whatever unique traits you desire. You’ll be amazed how well real-world situations can be modeled with object-oriented programming.

Making an object from a class is called instantiation, and you work with
instances of a class. In this chapter you’ll write classes and create instances
of those classes. You’ll store your classes in modules and import classes written by
other programmers into your own program files.

Learning about object-oriented programming will help you see the world as a programmer does.
It’ll help you understand your code—not just what’s happening line by line, but also the bigger concepts behind it.
Knowing the logic behind classes will train you to think logically, so you can write programs that effectively address almost any problem you encounter.

Classes also make life easier for you and the other programmers you’ll
work with as you take on increasingly complex challenges. When you and
other programmers write code based on the same kind of logic, you’ll be
able to understand each other’s work. Your programs will make sense to the
people you work with, allowing everyone to accomplish more .


-->

**Method:** A function that’s part of a class is a method.

**The __init__() method:** is a special method that Python runs automatically whenever we create a new instance based on the class.


### Importing classes:

* As you add more functionality to your classes, your files can get long, even 
when you use inheritance and composition properly. To help, Python lets you store classes in modules and then import 
the classes you need into your main program.

### Styling Classes :

* A few styling issues related to classes are worth clarifying, especially as your programs become more complicated.
* Class names should be written in CamelCase. To do this, capitalize the 
first letter of each word in the name, and don’t use underscores. 
* Instance and module names should be written in lowercase, with underscores between words.
* Every class should have a docstring immediately following the class definition. 
* The docstring should be a brief description of what the class does, and you should follow the same formatting conventions you used for writing docstrings in functions. Each module should also have a docstring describing what the classes in a module can be used for.
* You can use blank lines to organize code, but don’t use them excessively. Within a class you can use one blank line between methods, and within a module you can use two blank lines to separate classes.
* If you need to import a module from the standard library and a module that you wrote, place the import statement for the standard library module first. Then add a blank line and the import statement for the module you wrote. In programs with multiple import statements, this convention makes it easier to see where the different modules used in the program come from.


