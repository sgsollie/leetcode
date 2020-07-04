def same_structure_as(original,other):
    
    if not isinstance(original, list) or not isinstance(other, list):
        return False

    def recurse(arr):        
        listflag = False
        for i in range(len(arr)):
            if isinstance(arr[i], list):
                listflag = True
        
        if listflag == False:
            return []

        for i in range(len(arr)) :
            if type(arr[i]) is not list:
                arr[i] = None
            else:
                arr[i] = recurse(arr[i])
        return arr

    if recurse(original) == recurse(other):
        return True
    else:
        return False


#print(same_structure_as( [[1,0],[]]  ,  [[],[]]) )
print(same_structure_as( [1,[1,1]] , [[2,2],2] ))           # should be false