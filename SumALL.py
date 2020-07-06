#!/usr/bin/python3

import sys

# Other than the filename, you didn't say if it had to be a shell script or not, hence python :)

#arr = list(sys.argv)

def SumAll(arr):
    total = 0
    for i in range(1, len(arr)):
        total += int(arr[i])
    return total

print(SumAll(sys.argv))
