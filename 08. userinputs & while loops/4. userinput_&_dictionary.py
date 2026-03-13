# Filling a Dictionary with User Input
#* we can take user input as much as we want
#* lets do a poll, asking users about their favorite programming languages.

languages = {}
# Set a flag to indicate that polling is active.
flag = True

while flag:
    name = input("\nplease enter your name: ")
    fav_lang = input("\nplease enter your fav programming language: ")
    languages[name] = fav_lang
    
    another_poll = input("\ndo you want to take another poll. type 'yes/no': ")
    if another_poll == 'no':
        flag = False  

    
print(f"\npoll info are as follows:")
for key,val in languages.items():
    print(f"\t{key} : {val}")

#* The program first defines an empty dictionary (responses) and sets a flag (polling_active) to indicate that polling is active.
# As long as polling_active is True, Python will run the code in the while loop