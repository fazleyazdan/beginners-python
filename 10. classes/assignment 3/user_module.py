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