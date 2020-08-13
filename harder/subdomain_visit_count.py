
# Solution for https://leetcode.com/problems/subdomain-visit-count/submissions/

import re
from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)
        current = ""
        for i in cpdomains:
            subdomains = re.split(' |\.', i)[::-1]
            for j in range(len(subdomains)-1):
                if current == "" :
                    current += subdomains[j]
                else:
                    current = subdomains[j] + "." + current
                counts[current] += int(i.split(" ")[0])          
            current = ""
        
        outlst = []
        for names,hits in counts.items():
            outlst.append(str(hits) + " " + names)
        return outlst  
