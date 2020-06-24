
"""
Problem Statement
Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.

For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

Note: If a character is repeated, treat each occurence as distinct, for example an input of 'xxx' would return a list with 6 "versions" of 'xxx'

"""
def permute(s):
    
    out = []
    
    #base case
    if len(s) == 1:
        out = [s]
        
    else: 
        for i,letter in enumerate(s):                           
            for perm in permute(s[:i] + s[i+1:]):
                out += [letter+perm]
    
    return out


"""
iterations:
1. abc @ a permute(bc) # ab because s[:i] + s[i+1:] of abc at a is bc
                bc @ b permute(c)
                            returns c # cos len = 1
                        out = b+c
                out += a + bc #(['abc'])
                        
                bc @ c permute(b)
                            returns b # cos len = 1
                        out += [cb]
                out += a + cb #(['abc','acb'])


2. abc @ b permute(ac) # ab because s[:i] + s[i+1:] of abc at b is ac
                ac @ a permute(c) #hitting c here, because s[:i] + s[i+1:] of ac at a is c.
                            returns c # cos len = 1
                        out = a+c
                out += b + ac #(['abc','acb','bac'])

                ac @ c permute(a) #hitting a here because because s[:i] + s[i+1:] of ac at c is a. (s[i+1: would be null])
                            returns a # cos len = 1
                        out = c + a
                out += b + ca #(['abc','acb','bac','bca'])

3. abc @ c permute(ab) # ab because s[:i] + s[i+1:] of abc at c is ab
                ab @ a permute(b) # hitting b here because s[:i] + s[i+1:] of ab at a is b
                            returns b # cos len = 1
                    out = a + b
                out += c + ab #(['abc','acb','bac','bca','cab'])

                ab @ b permute(a) # hitting a here because s[:i] + s[i+1:] of ab at b is a
                            returns a # cos len = 1
                        out = b + a
                out += c + ba #(['abc','acb','bac','bca'])



"""


print(permute("abc"))