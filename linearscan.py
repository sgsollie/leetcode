def lin_scan(lst):
    
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i+1, len(lst)-1):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
                
    return lst

print(lin_scan([6,3,4,5,7,8,16,11,13,12]))

"""

"""