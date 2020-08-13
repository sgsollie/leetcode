"""
https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/

"""


class node(object):
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class stack(object):
    def __init__(self):
        self.items = []

    def push(self,val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)


def traversal(node):
    nodestack = stack()
    current = node

    while True:
        if current is not None:
            nodestack.push(current)
            current = current.left

        elif nodestack.size() > 0:
            current = nodestack.pop()
            print(current.key)
            current = current.right
        else:
            break

root = node(1) 
root.left = node(2) 
root.right = node(3) 
root.left.left = node(4) 
root.left.right = node(5) 

traversal(root) 


    