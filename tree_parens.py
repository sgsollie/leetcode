# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def tree2str(self,t: TreeNode) -> str:
        self.outstr = str(t.val)
        
        def traverse(root):
            if root:
                if root == t:
                    traverse(root.left)
                    traverse(root.right)
                else:
                    self.outstr += "(" + str(root.val)
                    traverse(root.left)
                    self.outstr += ")"
                    traverse(root.right)
            return self.outstr
        
        return traverse(t)



    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)

    a.left = b
    a.right = c
    a.left.left = d

    print(tree2str(a,a))