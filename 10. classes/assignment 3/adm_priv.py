from user_module import User

class Admin(User):
    
    def __init__(self, privileges):
        # self.privileges = privileges                                      #! uncomment this & the instances.  
        self.privileges_obj = Privileges(privileges)                        #! Privileges class Obj
    
        
    def show_privileges(self):
        print(f"Following are Admins privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")
            
# admin = Admin(['can add post', 'can add user'])
# admin.show_privileges()


print("\n------------ Task 3 ------------\n")

# Privileges: Write a separate Privileges class. 
# The class should have one attribute, privileges, that stores a list of strings like
# like "can add post", "can delete post", "can ban user", and so on. 
# Move the show_privileges() method to this class. 
# Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges

class Privileges:
    
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Following are Admins privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")
            