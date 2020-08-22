class Solution:
    def twoSum(self, nums, target: int):
        values = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in values: 
                return [values[compliment], i]
            values[nums[i]] = i

x = Solution()
print(x.twoSum([3,2,4],6))
                