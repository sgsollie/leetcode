"""
https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.
For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.
As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.


Time: O(n * n-1) I think - Iterating over each char, then for each char we are checking if it is in all chars previous and all chars afer n (so, not including n)

"""


def first_non_repeating_letter(strng):
    
    # Edge cases, return the string if it is empty or only one char
    if len(strng) <= 1:
        return strng
    if len(set(strng)) == 1:
        return ""
   
    outchar = ""
    
    for i in range(len(strng)):
        teststring = strng.lower()                                                              # Lowercase everything to enable easier checking
        if teststring[i] not in teststring[i+1:] and teststring[i] not in teststring[:i]:       # Check if char we are on occurs again, and if it occurs before
            outchar = strng[i]                                                                  # if it doesn't, this means it is unique, set it to a var for output - Use the original string to return correct case
            break                                                                               # we can break here because we only want the first unique char.
   
    return outchar

print(first_non_repeating_letter("moomen"))