def solution(string,markers):
    lst = string.split("\n")
    print(lst)
    
    markerset = set(markers)
    
    print(markerset)
    
    for i in range(len(lst)):
        intersection = list(markerset.intersection(lst[i]))
        if intersection:
            sep = intersection[0]
        #rest = text.split(sep, 1)[0]
            print(intersection)
            if i == lst[-1]:
                x = lst[i].partition(sep)
                lst[i] = x[0]
            else: 
                x = lst[i].partition(sep)
                lst[i] = x[0] + "\n"
                #lst[i] = lst[i][:chars.index(intersection[0])] + "\n"
        else:
            lst[i] = lst[i] + "\n"       
    print(lst)
    return "".join(lst)

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))