
"""
basic implementation of a bubble sort algorithm
"""

def bub_sort(lst):
     
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    
    return lst

print(bub_sort([10,7,5,23,9,111,22,3,4,5,2,1]))

"""
range over lst for elements 0 to 3,  (line 8 and 9 explanation)
      i = 0, j = 0, ranging over 0 to 3
      i = 0, j = 1, ranging over 0 to 3
      i = 0, j = 2, ranging over 0 to 3
      i = 0, j = 3, ranging over 0 to 3

      i = 1, j = 0, ranging over 0 to 2
      i = 1, j = 1, ranging over 0 to 2
      i = 1, j = 2, ranging over 0 to 2

      i = 2, j = 0, ranging over 0 to 1
      i = 2, j - 1, ranging over 0 to 1



"""
