"""
Pig latin.

Take a string of words. Move the first letter of each word to the end of it and add "ay" to the end of the word. Leave punctuation marks untouched.

Assumptions:
	Punctuation marks need to be left alone.
	String shouldn't contain numbers.
	There will be no more than one punctuation mark at the end of each word


1. Split the string into an array of words.
2. iterate over each element:
    a. Check if list element is just on element of punctuation on its own - if so, leave alone and continue
	b. If list element is a word, check if the word has punctuation on the end.
    c. if there is punctuation, remove it and store it somewhere then:
    d. Change each word to move the first letter to the end then add "ay" to the end of that word. 
    e. then, if punctuation, add that to the end of the word.


3. return joined list.


"""

import string

def pig_it(text):
    wordlst = text.split()
    
    validchars = set(string.ascii_letters)
    punc = ""
    
    for i in range(len(wordlst)):
        if len(wordlst[i]) < 1:
            continue
        if len(wordlst[i]) == 1 and wordlst[i][0] in validchars:
            wordlst[i] = wordlst[i] + "ay"
            continue
            
        if len(wordlst[i]) == 1 and wordlst[i][0] not in validchars:
            continue
            
        if wordlst[i][-1] not in validchars:
            punc = wordlst[i][-1]
            wordlst[i] = wordlst[i][:-1]
        wordlst[i] = wordlst[i][1:] + wordlst[i][0] + "ay" + punc
        punc = ""
        
    return " ".join(wordlst)
