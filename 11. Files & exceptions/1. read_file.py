""" 
Learning to handle exceptions will help you deal with situations in which files don’t exist and deal with 
other problems that can cause your programs to crash. This will make your programs more robust when
they encounter bad data, whether it comes from innocent mistakes or from malicious attempts to break your programs.

"""

#* When you want to work with the information in a text file, the first step is to read the file into memory. 
#* You can then work through all of the file’s contents at once or work through the contents line by line.

""" 
To begin, we need a file with a few lines of text in it. Let's start with a file 
that contains pi to 30 decimal places, with 10 decimal places per line:
 
3.1415926535
  8979323846
  2643383279

"""

from pathlib import Path

path = Path("pi_digits.txt")         
content = path.read_text()
print(content)