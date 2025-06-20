""" 
Learning to handle exceptions will help you deal with situations in which files don't exist and deal with 
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

path = Path("pi_digits.txt")         # since the file exists in the same path, file name is all you need to pass  
content = path.read_text()
print(content)

""" 
 To work with the contents of a file, we need to tell Python the path to 
the file. A path is the exact location of a file or folder on a system. Python 
provides a module called pathlib that makes it easier to work with files and 
directories,

There's a lot you can do with a Path object that points to a file. 
For example, you can check that the file exists before working with it, 
read the file's contents, or write new data to the file.

"""