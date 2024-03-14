# this code prints pairs of names from the friends list in the format "First_Name Last_Name". 
# Note that this code assumes that the number of names is even and that each name consists of a first name and a last name. 
# If the number of names is odd or if names are formatted differently, the code may not behave as expected.
# friends = """ ... """.split(): This creates a multiline string with names separated by newlines 
# and then uses the split() method to convert it into a list of names. Each name becomes an element in the list.

friends = """Coral Alfaro
Phillip Ryan
Alfred Odling
Cohan Gardner
Bradley Fisher
Jenny Marshall
Meredith Connolly
Cassia Simons
Maegan Terrell
Fox Branch
Nichola Hale
Saskia Allison
Calista Brennan
Petra Naylor
Anita Lane
Patrik Guy
Lillia Salgado
Hadiya Mcbride
Ashton Mcdonnell
Rex Chambers
Sama Rios
Jarrad Sweet
Jokubas Davenport
Kathy Cooke
Alison Duke
Aneesa Garner
Dalia Bartlett
Yisroel Griffiths
Yara Redfern
Wiktoria Kearney
Alex Cooley
Sylvie Todd
Eren Moon
Aya Pitt
Lynda Banks
Lola Lucas
Eve Shah
""".split()

# print(friends)
print(len(friends))

for i in range(int(len(friends)/2)):               # (int(len(friends)/2)): this will iterate half of the list (will iterate first names)
    print(friends[2*i] +" "+ friends[2*i+1])       # friends(2*i+1): this will iterate the last name and will concatenate it with f.name
 