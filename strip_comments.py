"""

Working solution for https://www.codewars.com/kata/51c8e37cee245da6b40000bd

"""

def solution(string,markers):
    lst = string.split("\n")
    print(lst)
    
    markerset = set(markers)
    
    print(markerset)
    
    for i in range(len(lst)):
        intersection = list(markerset.intersection(lst[i]))
        if intersection:
            for j in range(len(intersection)):
                sep = intersection[j]
                if i == len(lst)-1:
                    x = lst[i].partition(sep)
                    lst[i] = x[0].rstrip()
                else: 
                    x = lst[i].partition(sep)
                    lst[i] = x[0].rstrip() + "\n"
        elif i == len(lst)-1:
            lst[i] = lst[i].rstrip()
        else: 
            lst[i] = lst[i].rstrip() + "\n"

    print(lst)
    return "".join(lst)

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))