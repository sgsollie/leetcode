"""


The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position.

Put together these modified chunks and return the result as a string.

If sz is <= 0 or if str is empty return ""
If sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".

"""

import re

def revrot(strng, sz):

    #Edge cases
    if sz > len(strng) or sz <= 0 or strng == None:
        return ""
    #Use regex to break down the chunks
    lst = re.findall('\d{'+ str(sz) +'}', strng)
    
    for i in range(len(lst)):
        sumlist = []
        sum = 0
        for digit in lst[i]:
            sumlist.append(int(digit) ** 3)             # get powers of 3 for each digit and put them in a list
        for j in sumlist:
            sum += j                                    # Add together the powers of 3 and chek if they're divisible by 2
        if sum % 2 == 0:
            lst[i] = lst[i][::-1]                       # If they're divisible by 2, change the chunk's list entry to the reversed chunk
        else: 
            rotated = lst[i][1:] + lst[i][0]            # Else: if it insn't divisible by 2: Requrement to rotate the chunk (ie move first char to the back)
            lst[i] = rotated                            # Put the rotated chunk back in the list, in place of the original
        sumlist = []
        sum = 0

    return "".join(lst)                                 # rejoin the list to return it as one string
    

print(revrot("423456789", 2))