"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" 
if that character appears only once in the original string, or ")" if that character appears more than once in 
the original string. Ignore capitalization when determining if a character is a duplicate.

Assumptions:
    Can include special characters
    must ignore capitalization


1. Make input string lower case
2. initialise an empty dict which we will use to count how many times we find a letter
3. iterate over each character in input string. Add the letter to the dict and a count of 1
4. if we come across a letter we've already seen, append the count value of that index in the dict
5. iterate over each character again. Check how many times we've seen it in the first pass
6. Generate an output string by appending either "(" or ")" based on how many times we've seen this char 

Time Complexity - O(n^2)
Space Complexity - O(n)

"""

def duplicate_encode(word):
    wordmap = {}
    output = ""
    
    word = word.lower()
    
    for i in word:
        wordmap[i] = wordmap.get(i, 0) + 1
    
    for i in word:
        if wordmap[i] > 1:
            output += ")"
        else:
            output += "("
        
    return output