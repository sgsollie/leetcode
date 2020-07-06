# Answer for online coding question at Self driving car startup.

import re
import sys

filename = input()

bytesname = "bytes_" + filename
open(bytesname, "a+")

bigcount = 0
sumcount = 0

with open(filename, "r" ) as infile:
    for line in infile:                                                 # This sucks, we should run the regex on the whole file and work with lines that match
        if re.search('\d+$', line):
            sizereq = int(re.search('\d+$', line).group(0))
            if sizereq > 5000 :
                print(line,sizereq)
                bigcount += 1
                sumcount += sizereq
    
    f = open(bytesname, "a+")
    f.writelines([str(bigcount), "\n" + str(sumcount)])
    f.close()