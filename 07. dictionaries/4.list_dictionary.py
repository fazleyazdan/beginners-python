# Rather than putting a dictionary inside a list, it’s sometimes useful to put a list inside a dictionary

list_dictionary = {'brand': 'toshiba',
                   'specs': ['i9', '16 GB RAM', '500 GB SSD']}

print(f"you have orderd {list_dictionary['brand']} with the following specs")
for content in list_dictionary['specs']:
    print(f"\t{content}")                              #! \t for indentation
    

#* You can nest a list inside a dictionary anytime you want more than one value to be associated with a single key
# In the earlier example of favorite programming languages, if we were to store each person’s responses in a list, 
#* people could choose more than one favorite language. Dictionaries   When we loop through the dictionary, 
# the value associated with each peeson would be a list of languages rather than a single language. 
#* Inside the dictionary’s for loop, we use another for loop to run through the list of languages associated with each person:

fav_languages = {'fazleyazdn': ['python', 'JS'],
                 'jawad': ['c', 'rust'],
                 'Hameed': ['JS'],
                 'shadman': ['dot net', 'c#'],
                 'ali': ['ruby']}

for name,languages in fav_languages.items():
    print(f"\n{name.title()}'s fav lamnguages are:")
    for language in languages:
        print(f"\t{language.title()}") 
        
#* To refine this program even further, you could include an if statement 
# at the beginning of the dictionary’s for loop to see whether each person has 
#* more than one favorite language by examining the value of len(languages). 
# If a person has more than one favorite, the output would stay the same. 
#* If the person has only one favorite language, you could change the wording to 
# reflect that. For example, you could say, “Sarah’s favorite language is C.”

print("\nafter refining the dictionary")
for name,languages in fav_languages.items():
    if len(languages)>1:
        print(f"\n{name.title()}'s fav languages are:")
        for language in languages:
            print(f"\t{language.title()}") 
    else:
        print(f"\n{name.title()}'s fav language is {language.title()}")