# Printing Models: Put the functions for the example printing_models.py in a 
# separate file called printing_functions.py. Write an import statement at the top 
# of printing_models.py, and modify the file to use the imported functions.

# from printing_functions import print_models

#! using different import approaches.
import printing_functions
import printing_functions as pf
from printing_functions import print_models
from printing_functions import print_models as pm
from printing_functions import *

my_designs = ['3D', 'Graph', 'linear']
str_design = []

# printing_functions.print_models(my_designs,str_design)                  #! for: import printing functions
print_models(my_designs,str_design)
print(f"\nPrinted Designs are : {str_design}")