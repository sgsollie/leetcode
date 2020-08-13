"""
iterative:
iterate throigh each char.
create a set of numbers
If we get to a number. Check if all chars from position to end are numbers


"""

def increment_string(strng):
    
    if strng == "":
        return strng + "1"
        
    nums = list("0123456789")
    sum = []
    zerocounter = 0
    
    for i in range(len(strng)):
        if strng[i] in nums:
            sum.append(int(strng[i]))
    
    #print(sum) 
    l = len(sum)
    print("numbers on end: ",l)
    if l == 0:
        return strng + "1"
    else:
        end = int("".join(map(str, sum))) + 1
        print("end = ",end)
    
    zerocounter += l - len(str(end))
        
    print("input: ", strng)
    
    if len(str(end)) >= l:
        return strng[:-l] + str(end)    ## todo, fix leading zeroes. Perhaps loop over len(end) and add zeroes until it matches len(sum)
    elif len(str(end)) < l:
        return strng[:-l] + "0" * zerocounter  + str(end)
        


print(increment_string("foobar001"))
print()
print(increment_string("foobar010"))
print()
print(increment_string("foobar099"))
print()
print(increment_string("foobar032040499"))
