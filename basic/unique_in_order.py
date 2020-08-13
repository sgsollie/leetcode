"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of
items without any elements with the same value next to each other and preserving the original order of elements.

eg: 
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]

First algorithm:
Create an empty list, which we will return.

Add the first character in the iterable to the list.
As we iterate through, check the char we are on to see if it is the same as the previous char:
If it is not, add that char to the list by appending it. 

Finish loop. Return the list.
O(n) time.


"""

def unique_in_order(iterable):
    mylst = []
    for i in range(len(iterable)):
        if i == 0:
            mylst.append(iterable[i])
        elif iterable[i] != iterable[i-1]:
            mylst.append(iterable[i])
            
    return mylst