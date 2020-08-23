
# Solution for: https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.insert(index[i],nums[i])
        return output 
        