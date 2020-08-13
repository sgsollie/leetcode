"""
Partial solution for https://leetcode.com/problems/making-file-names-unique/

Not yet solved: ["gta","gta(1)","gta","avalon"] edge case.

Saving this potentially useful regex here too: #name = re.search('.+?(?=\()', i).group(0) - which matches chars up to first "("

"""

import re

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        seen = {}
        output = []
        for i in names:
            seen[i] = 1
        
        for i in seen:
            occurance = seen[i]
            if occurance < 2:
                output.append(i)
            else:
                for j in range(occurance):
                    if j == 0:
                        output.append(i)
                else:
                    output.append(i + "(" + str(j) + ")")
        return output
        
            
