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


