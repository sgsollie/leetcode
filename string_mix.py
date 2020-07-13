from collections import Counter

def mix(s1, s2):
    s1d = {}
    s2d = {}

    for i in s1:
        if i.islower():
            s1d[i] = s1d.get(i, 0) + 1
    
    for i in s2:
        if i.islower():
            s2d[i] = s2d.get(i, 0) + 1
          

    if len(s1d) > len(s2d):
        longest = s1d
        shortest = s2d
    else:
        longest = s2d
        shortest = s1d

    Cdict = Counter(s1d) + Counter(s2d) 
    print(Cdict) 
          
   # print(longest) 

    outlst = []

    for i in Cdict:
        if i in s1d and i in s2d:
            if s1d[i] > s2d[i]:
                prefix = "1:"
            elif s1d[i] < s2d[i]:
                prefix = "2:"
            elif s1d[i] == s2d[i]:
                prefix = "=:"
            most = max(shortest[i], longest[i])
            if most > 1:    
                outlst.append(prefix + i * most)
        else:
            if Cdict[i] > 1:
                if i in s1d:
                    outlst.append("1:" + i * Cdict[i])
                else:
                    outlst.append("2:" + i * Cdict[i])

    outlst.sort()
    outlst.sort(key=len,reverse=True)

    return "/".join(outlst)

print(mix("In many languages", "there's a pair of functions"))
