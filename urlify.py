"""
Write a method to replace all spaces in a string with '%20'
"""

"""
Take the string, iterate over each element (character), 
for each character, we will check if it is a space.
If it is a space,  copy the string up to what we have so far, and place this in a new array/list
then, we will append "%20" to that array. 
After which, we append the rest of the string to this new array
repeat for each iteration.

Time Complexity: O(N)
Space Complexity: O(N)

"""

def urlify(str1, trueLength):
    newstring = ''
    index = 0
    for i in range(trueLength):
        if str1[i] == ' ':
            newstring += str1[index:i]
            newstring += '%20'
            index = i + 1
    newstring += str1[index:]
    return newstring

print(urlify("Mr John Smith", 13))