# check if a word is palindrome or not
# use 'racecar' as an example

def check_if_palindrome(word):
     n = len(word)
     for i in range(n//2):                  #! n // 2 : // is used for rounding: this operation also know as 'floor division'
         if word[i] != word[n- i- 1]:
             return False
         else:
             return True

word = 'racecar'
print(f"{word} is palindrome:", check_if_palindrome(word))




# How the -1 Works in Indexing:
#* Length of the String:

#* n = len(s) gets the length of the string s.
# Loop through the String:

#* for i in range(n // 2) loops from 0 to n // 2 - 1, which is the midpoint of the string. This ensures we only compare each pair of characters once.
# Character Comparison:

#* s[i] accesses the character at index i from the start of the string.
# s[n - i - 1] accesses the character at index n - i - 1 from the end of the string.
# For i = 0, s[i] is the first character and s[n - i - 1] is the last character.
# For i = 1, s[i] is the second character and s[n - i - 1] is the second-to-last character.
# This continues until the midpoint of the string.

