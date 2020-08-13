
# Solution for https://leetcode.com/problems/same-tree/

"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        l1 = []
        l2 = []
        
        
        def traverse(root,lst):
            if root:
                lst.append(root.val)
                traverse(root.left,lst)
                traverse(root.right,lst)
            else:
                lst.append(None)
            return
        
        traverse(p,l1)
        traverse(q,l2)
        return l1 == l2