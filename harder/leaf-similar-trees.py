
# Solution for https://leetcode.com/problems/leaf-similar-trees
"""

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        lvs1 = []
        lvs2 = []                                                   # Initialise two empty lists to store leaf values for each tree
        
        def traverse(root: TreeNode, lvs: list):
            if not root: return
            if not root.left and not root.right:                    # If there are no children we have a leaf. 
                lvs.append(root.val)                                # Append the leaf to the relevant list
                return              
            traverse(root.left,lvs)        
            traverse(root.right,lvs)
            return
        
        traverse(root1,lvs1)                                        # Traverse both trees to get the leaves
        traverse(root2,lvs2)

        return lvs1 == lvs2                                         # Return true or false based on if the two lists match or not