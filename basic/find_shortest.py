"""
Function to find shortest word in a string (where words are separated by spaces)
Not using python's min function - writing an algo to do it instead.

"""

def find_short(s):
    lst = s.split()                 # easiest way to split words up in python separated by spaces

    l = lst[0]                      # give us a starting point
    
    for i in range(len(lst)):       # range over the list of strings
        if len(lst[i]) < len(l):    # if the length of the string we are on is less than l, set l to be this shorter string
            l = lst[i]
    
    return len(l)                   # l: shortest word length
    
print(find_short("These are some words to try a test with"))