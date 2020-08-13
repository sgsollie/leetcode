"""
Reversal of a string by iterating over it backwards

"""


def reversal(strng):
    i = len(strng) -1               # Make counter the length of the string minus 1. As we decrement, zero is included
    newstring = ""                  # Initialise a blank new string

    while i >= 0:                   
        newstring += strng[i]       # append the new string with each letter (so for "ollie" we start at strng[4] (e)
        i -=1                       # decrement the counter to move the index back a position
    
    return newstring
print(reversal("ollie"))
