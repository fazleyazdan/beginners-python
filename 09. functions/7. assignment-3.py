# Write a function called city_country() that takes in the name of a city and its country. 
# The function should return a string formatted like this:
'''------------------------
    "Santiago, Chile"
   ------------------------'''
# Call your function with at least three city-country pairs, and print the values that are returned

def city_country(city_name, country):
    return (f"\n------------------------------------\n\t{city_name}, {country}\n------------------------------------")

print(city_country('islamabad', 'pakistan'))
print(city_country('Madina', 'Saudi Arabia'))
print(city_country('Peshawar', 'Pakistan'))


#! ==================== Task 2 ==================== #

#* Album: Write a function called make_album() that builds a dictionary describing a Nasheed album. 
# The function should take in an artist name and an album title, 
# and it should return a dictionary containing these two pieces of information. 
# Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the dictionaries are storing the album information correctly.
#* Use None to add an optional parameter to make_album() that allows you to store the number of Nasheeds on an album. 
# If the calling line includes a value for the number of Nasheeds, add that value to the album’s dictionary. 
# Make at least one new function call that includes the number of Nasheeds on an album.

def make_album(artist_name,title, num_nasheeds = None):
    if num_nasheeds:
        album = {'artist': artist_name.title(), 'album_title': title, 'num of nasheeds': num_nasheeds}
    else:
        album = {'artist': artist_name.title(), 'album_title': title}
        
    return album

print(make_album('ahmad Bukhatir','last breath'))
print(make_album('ihsan tehmeed','tammana'))
print(make_album('junaid jamshed','traveller of this world'))

#* calling with optional parameter
print(make_album('zafar ullah qasmi','fasily', '7'))


#! ==================== Task 3 ==================== #
#* User Albums: Start with your program from the above task.
# Write a while loop that allows users to enter an album’s artist and title. 
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
# Be sure to include a quit value in the while loop.


while True:
    print(f"\nEnter 'q' at anytime to quit")
    str_art_name = input("Please enter an artist name: ")
    if str_art_name == 'q':
        break
    str_title = input("Please enter an album title: ")
    if str_title == 'q':
        break
    str_nasheeds = input("Please enter number of nasheeds (Leave empty if there are none): ")
    if str_nasheeds == 'q':
        break
    print(f"\n{make_album(str_art_name,str_title,str_nasheeds)}")