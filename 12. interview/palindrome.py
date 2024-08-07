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