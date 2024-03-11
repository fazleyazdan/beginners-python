# ==================== Task 1 ==================== #

#* T-Shirt: Write a function called make_shirt() that accepts a size and the 
# text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments

def make_shirt(size, message):
    print(f"\nprint {message.title()} on a {size.title()} size shirt")
    
# calling with positional args
make_shirt('medium', "'be kind'")

# calling with keyword args
make_shirt(size='large', message="'be original in this fake world'")


#! ==================== Task 2 ==================== #
#* Large Shirts: Modify the make_shirt() function so that shirts are large 
# by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

#* default size
def make_shirt_1(message, size = 'large'):
    print(f"\nprint '{message}' on a {size} size T-shirt")
make_shirt_1('I love python')

#* default message
def make_shirt_2(size, message = 'i love programming'):
    print(f"\nprint '{message}' on a {size} size T-shirt")
make_shirt_2(size = 'large')
make_shirt_2(size='medium')

#*different message
make_shirt_2(size='small', message='peace be upon you')