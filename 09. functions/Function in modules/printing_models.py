# Printing Models: Put the functions for the example printing_models.py in a 
# separate file called printing_functions.py. Write an import statement at the top 
# of printing_models.py, and modify the file to use the imported functions.

from printing_functions import print_models

my_designs = ['3D', 'Graph', 'linear']
str_design = []

print_models(my_designs,str_design)
print(f"\nPrinted Designs are : {str_design}")