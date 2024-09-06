# Count Vowels in a String

# Problem: Write a Python function that counts the number of vowels in a given string.
# Input: A string s.
# Output: An integer representing the number of vowels (a, e, i, o, u) in the string.


vowels = ['a', 'e','i', 'o','u']                # keep vowels in a list
                                                
def count_vowels(word):             
    vowels_count = 0                            # counter for vowels
    for i in range(len(word)):
        if word[i] in vowels:                   # loop through the vowels
            vowels_count += 1                   
        # else:                                 # it is better not to write else-continue statement....                 
            # continue                          # because if there is no 'else' block, by default only if is entertained. 
    return vowels_count

print(count_vowels('aeiou'))



