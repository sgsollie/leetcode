"""

O(n) solution for https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        outbools = []
        for i in candies:
            if i + extraCandies >= max(candies):
                outbools.append(True)
            else: 
                outbools.append(False)
        return outbools