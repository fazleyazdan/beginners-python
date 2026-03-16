# Rather than putting a dictionary inside a list, it’s sometimes useful to put a list inside a dictionary

list_dictionary = {'brand': 'toshiba',
                   'specs': ['i9', '16 GB RAM', '500 GB SSD']}

print(f"you have orderd {list_dictionary['brand']} with the following specs")
for content in list_dictionary['specs']:
    print(f"\t{content}")                              #! \t for indentation
    

