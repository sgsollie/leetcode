"""
Function to check if a balanced binary tree is a binary search tree

"""


class tree(object):
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def preOrder(tree):
    if tree.left == None or tree.right == None:                             # Only works for a balanced tree
        return
    else:
        print(treecheck(tree))
        preOrder(tree.left) 
        preOrder(tree.right)

def treecheck(tree):
    if tree.left.key <= tree.key and tree.right.key > tree.key:
        return True
    else:
        return False

print("Valid BST: ")
r = tree(5)
r.left = tree(3)
r.left.left = tree(2)
r.left.right = tree(4)
r.right = tree(7)

print()

print("Invalid BST :")
t = tree(5)
t.left = tree(6)
t.right = tree(4)
preOrder(t)

