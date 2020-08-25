"""

Solution for https://leetcode.com/problems/split-a-string-in-balanced-strings/

Time Complexity: O(n)
Space Complexity: O(n)

1. Iterate over input string s. Check if it is an "L" - we know from constraints it can only be "L" or "R"
2. Use two variables as counters. Increment either the L counter or the R counter depending on what letter we see
3. If the L and R counters match that means we know we have the same amount of both letters so we must have found a balanced substring
4. Append the output counter with our finding. Reset L and R counters and repeat the above until we get to the end of input string.

"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lcount, rcount, output = 0,0,0
        
        for i in range(len(s)):
            if s[i] == "L":
                lcount += 1
            else:
                rcount += 1
            
            if lcount == rcount:
                output += 1
                lcount = 0
                rcount = 0
        
        return output