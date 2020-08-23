"""

Solution for code kata: https://www.codewars.com/kata/55e1d2ba1a3229674d000037

Linked Lists - Front Back Split

Write a FrontBackSplit() function that takes one list and splits it into two sublists — one for the front half, and one for the back half. 
If the number of elements is odd, the extra element should go in the front list. For example, FrontBackSplit() on the list 2 -> 3 -> 5 -> 7 -> 11 -> null should yield the two lists 2 -> 3 -> 5 -> null and 7 -> 11 -> null. 
Getting this right for all the cases is harder than it looks. You will probably need special case code to deal with lists of length < 2 cases.

"""


""" For your information:
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
"""

import math

def front_back_split(source, front, back):
    # Raise errors if we don't have correct inputs
    if source == None or front == None or back == None or source.next == None:
        raise TypeError
    
    # Walk the linked list and record the length
    sourcelen = 1
    walksource = source
    while walksource.next != None:
        sourcelen += 1
        walksource = walksource.next
        
    # Deal with edgecases if the list is only two nodes - split it down the middle
    if sourcelen == 2:
        back.data = source.next.data
        front.data = source.data
        front.next = None
        return front, back
    

    # Snip the source list in half and set the halves as front and back
    if sourcelen %2 == 0:
        frontlen = sourcelen // 2               # frontlen will be the length of the first half. 
    else:
        frontlen = math.ceil(sourcelen / 2)     # This satisfies the requirement of the remainder (if list is odd length) being added to the front
        
    front.data = source.data
    front.next = source.next
    while frontlen > 1:                         # Walk the first half only
        source = source.next
        frontlen -= 1
    back.data = source.next.data                # Set the beginning of back as the next node along from the end of the first half
    back.next = source.next.next
    source.next = None                          # Snip here.
    
    return front, back