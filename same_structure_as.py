def same_structure_as(original,other):
    
    if not isinstance(original, list) or not isinstance(other, list):
        return False

    if len(original) != len(other):
        return False
    
    def recurse(arr):
        count = 0        
        listflag = False
        for i in range(len(arr)):
            count += 1
            if isinstance(arr[i], list):
                listflag = True
        
        if listflag == False:
            count += 1
            return count, []

        for i in range(len(arr)) :
            if type(arr[i]) is not list:
                count += 1
                arr[i] = None
            else:
                arr[i] = recurse(arr[i])
                count += 1
        return count,arr

    count1, firstarr = recurse(original)
    count2, secondarr = recurse(other)
    print(count1, firstarr)
    print(count2, secondarr)


    if count1 == count2 and firstarr == secondarr:
        return True
    else:
        return False


#print(same_structure_as( [[1,0],[]]  ,  [[],[]]) )
print(same_structure_as( [1,[1,1]] , [2,[2]] ))           # should be false