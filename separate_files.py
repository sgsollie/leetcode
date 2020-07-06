# Answer for online coding question at Self driving car startup.

import os
import sys
import re

baseFilename = input()
with open(baseFilename, "r") as infile:
    for line in infile:
        if re.search('.cpp$|.cs$|.c$', line):
            extension = re.search('.cpp$|.cs$|.c$', line).group(0)
            if extension == ".cpp":
                filename = "cpp_" + baseFilename
                f=open(filename, "a+")
                f.write(line)
            elif extension == ".cs":
                filename = "cs_" + baseFilename
                f=open(filename, "a+")
                f.write(line)
            elif extension == ".c":
                filename = "c_" + baseFilename
                f=open(filename, "a+")
                f.write(line)
            f.close()