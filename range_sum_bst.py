
# Solution for https://leetcode.com/problems/range-sum-of-bst/solution/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""

We traverse the tree using a depth first search. If node.val falls outside the range [L, R], 
(for example node.val < L), then we know that only the right branch could have nodes with value inside [L, R].

"""

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.total = 0
        def traverse(root):
            if not root:
                return 0  
            if root.val in range(L,R+1):    
                self.total += root.val      
            if L < root.val:
                traverse(root.left)
            if root.val < R: 
                traverse(root.right)
            return self.total
        
        traverse(root)
        return self.total