# Login Attempts: Add an attribute called login_attempts to your User class from assignment 1 Task 3. 
# Write a method called increment_login_attempts()
# that increments the value of login_attempts by 1. Write another method called 
# reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()several times. 
# Print the value of login_attempts to make sure it was incremented properly, 
# and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.


class User():
    
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        
    def describe_user(self, age, profession):
        print(f"\tUser name: {self.first_name + ' ' + self.last_name}")
        print(f"\tUser age: {age}")
        print(f"\tUser profession: {profession}")
        
    def greet_user(self):
        print(f"\nHello {self.first_name + ' ' + self.last_name}! Welcome to beginners Python")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
    
user = User('fazle', 'yazdan')

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"\nLogin attempts by the user are: {user.login_attempts}")

user.reset_login_attempts()
print(f"\nLogin attempts by the user after resetting: {user.login_attempts}")
