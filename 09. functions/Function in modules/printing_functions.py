# Consider a company that creates 3D printed models of designs that users submit. 
# Designs that need to be printed are stored in a list, and after being printed they're moved to a separate list.

def print_models(designs, storing_design):
    designs.reverse()                  #! as pop remove last items from the list. reversed it so the first item is removed & printed
    while designs:
        printing = designs.pop()
        print(f"\nprinting design {printing}")
        storing_design.append(printing)
    return storing_design

# my_designs = ['3D', 'Graph', 'linear']
# str_design = []

# print_models(my_designs,str_design)
# print(my_designs)
# print(str_design)