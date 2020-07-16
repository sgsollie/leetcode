
# Working recursive solution for: https://leetcode.com/problems/construct-string-from-binary-tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t == None:
            return ""

        self.outstr = str(t.val)
        
        def traverse(root):
            if root:
                if root == t:
                    if not root.left and not root.right:
                        return str(root.val)
                    if root.left:
                        traverse(root.left)
                    else:
                        self.outstr += "()"
                    if root.right:
                        traverse(root.right)
                else:
                    self.outstr += "(" + str(root.val)
                    if root.left:
                        traverse(root.left)
                    if not root.left and root.right:                # Some duplication of efforts here by the looks of it
                        self.outstr += "()"
                    if root.right:
                        traverse(root.right)
                    self.outstr += ")"

            return self.outstr
        
        return traverse(t)



    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)

    a.left = b
    #a.right = c
    a.left.left = c
    a.left.right = d

    print(tree2str(a,a))