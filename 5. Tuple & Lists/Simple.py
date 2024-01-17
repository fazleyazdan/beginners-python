# define a tuple named dimensions in Python. In this specific case, the tuple contains two elements: 200 and 50. 
# Tuples are similar to lists but are immutable, meaning their elements cannot be modified after the tuple is created.

dimensions = (200,50)

print(f"first dimension is: {dimensions[0]}")

# dimensions [0] = 250                  # this will give error. because tuple is immutable

# you can reassign a tuple for e.g

dimensions = (100,200)
print(f"first dimension is: {dimensions[0]}")
