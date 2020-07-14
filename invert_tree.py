
# Recursive solution for https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return                                    # Leetcode likes to test with null params
        if not root.left and not root.right:                   # base case - if we've not got any children just send the node back
            return root
        
        t = self.invertTree(root.right)                        # swapsies, t stands for temp. Swap the recursive case of root.left and root.right
        root.right = self.invertTree(root.left)                # Assign right to a temp variable first since editing in place wouldn't work
        root.left = t
        
        return root                                            # return the node