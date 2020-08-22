"""

O(n) Solution for https://leetcode.com/problems/shuffle-string/submissions/

"""

class Solution:
    def restoreString(self, s: str, indices):
        output = [''] * len(s)
        for i in range(len(s)):
            output[indices[i]] = s[i]
        return "".join(output)

x = Solution()
print(x.restoreString("codeleet",[4,5,6,7,0,2,1,3]))